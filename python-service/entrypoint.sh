#!/bin/bash

set -euo pipefail

alembic upgrade head

python main.py
