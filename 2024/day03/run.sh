#!/bin/bash
PYTHONDONTWRITEBYTECODE=1 uv run ptw -c --ignore .venv --ext .txt,.py -- -s -raFP -W ignore::pytest.PytestReturnNotNoneWarning -p no:cacheprovider
