"""openclaw_provider_key derivation.

Lives in its own module to avoid circular imports between the clients and
the api package __init__.
"""
# openclaw's actual convention uses 'comet-' (no 'api') for the cometapi
# provider. The internal provider_id stays "cometapi" (in providers.json and
# throughout this codebase) so the URLs and env vars keep matching, but when
# we emit the openclaw_provider_key field we translate to OpenClaw's form.
OPENCLAW_KEY_PROVIDER_ALIASES = {
    "cometapi": "comet",
}


def openclaw_provider_key(provider_id: str, api_type: str | None) -> str | None:
    """Derive an openclaw_provider_key from the internal provider_id and the
    resolved api_type. Returns None if api_type is None/empty.

    Default rule: ``{provider_id}-{api_type}`` (lowercase). The only exception
    is ``cometapi`` → ``comet`` to match OpenClaw's actual config convention.
    """
    if not api_type:
        return None
    openclaw_pid = OPENCLAW_KEY_PROVIDER_ALIASES.get(provider_id, provider_id)
    return f"{openclaw_pid}-{api_type}"
