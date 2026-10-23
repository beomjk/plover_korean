"""Checks that the Korean tutorial matches what Plover outputs with this plugin."""

import sys
from pathlib import Path

import pytest

TUTORIAL_DIR = Path(__file__).resolve().parent.parent / 'docs' / 'tutorial'
sys.path.insert(0, str(TUTORIAL_DIR / 'tools'))

# Building a page types every example through Plover and fails on a mismatch.
import build_tutorial  # noqa: E402


@pytest.mark.parametrize('name', sorted(build_tutorial.FILES))
def test_tutorial_is_up_to_date(name):
    shipped = (TUTORIAL_DIR / name).read_text(encoding='utf-8')
    assert shipped == build_tutorial.FILES[name](), \
        'Regenerate with: uv run python docs/tutorial/tools/build_tutorial.py'
