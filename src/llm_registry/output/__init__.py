# SPDX-License-Identifier: MIT
"""Output module."""
from llm_registry.output.writer import (
    generate_markdown,
    get_timestamp,
    read_models_json,
    write_models_json,
)

__all__ = ["generate_markdown", "get_timestamp", "read_models_json", "write_models_json"]
