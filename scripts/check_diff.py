#!/usr/bin/env python
# SPDX-License-Identifier: MIT
"""Check two MODELS.json snapshots for suspicious differences."""

from __future__ import annotations

import sys

from llm_registry.diff_cli import main


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
