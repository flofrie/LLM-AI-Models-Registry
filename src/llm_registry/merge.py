"""Merge helpers for model registry updates."""

from typing import TypeVar

from pydantic import BaseModel

from llm_registry.schema.model_entry import ModelEntry

T = TypeVar("T", bound=BaseModel)


def merge_model_entries(existing: ModelEntry, new: ModelEntry) -> ModelEntry:
    """Merge a fresh entry into an existing registry entry.

    Only fields explicitly provided on ``new`` (tracked via ``model_fields_set``)
    participate in the merge. Pydantic defaults — e.g. ``available=True``,
    ``deprecated=False`` — are **not** treated as fresh provider data, so a
    stripped API entry cannot clear existing manual state. Null values for
    explicitly-set Optional fields still preserve existing data. Nested
    Pydantic models are merged field-by-field so partial API data cannot erase
    enriched pricing or capability subfields.
    """
    return _merge_model(existing, new)


def mark_missing_provider_models_unavailable(
    models: dict[str, ModelEntry],
    provider_id: str,
    fresh_entries: list[ModelEntry],
    timestamp: str,
) -> int:
    """Soft-delete provider models absent from a successful discovery run.

    Replaces changed entries in the dict instead of mutating them in place,
    matching the copy-on-merge contract used by ``merge_model_entries``.
    """
    fresh_model_ids = {entry.model_id for entry in fresh_entries}
    note = f"No longer listed by provider as of {timestamp}"
    changed = 0

    for key, entry in models.items():
        if entry.provider != provider_id:
            continue
        if entry.model_id in fresh_model_ids:
            continue
        if entry.available is False:
            continue

        updated = entry.model_copy(deep=True)
        updated.available = False
        updated.notes = f"{updated.notes.rstrip()}\n{note}" if updated.notes else note
        models[key] = updated
        changed += 1

    return changed


def _merge_model(existing: T, new: T) -> T:
    merged = existing.model_copy(deep=True)
    explicitly_set = new.model_fields_set
    for field_name in type(new).model_fields:
        # Skip Pydantic defaults: an entry built without a value for this field
        # carries no fresh information, so it must not clobber existing data.
        if field_name not in explicitly_set:
            continue

        new_value = getattr(new, field_name)
        if new_value is None:
            continue

        existing_value = getattr(existing, field_name, None)
        if isinstance(new_value, BaseModel):
            if not _has_present_value(new_value):
                continue
            if isinstance(existing_value, type(new_value)):
                setattr(merged, field_name, _merge_model(existing_value, new_value))
            else:
                setattr(merged, field_name, new_value.model_copy(deep=True))
            continue

        setattr(merged, field_name, new_value)

    return merged


def _has_present_value(model: BaseModel) -> bool:
    for field_name in type(model).model_fields:
        value = getattr(model, field_name)
        if isinstance(value, BaseModel):
            if _has_present_value(value):
                return True
        elif value is not None:
            return True
    return False
