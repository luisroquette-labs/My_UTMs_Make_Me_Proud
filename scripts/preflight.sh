#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validar-tracking-link.py --self-test
PYTHONDONTWRITEBYTECODE=1 python3 scripts/gerar-dashboard.py --self-test
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_comments.py
