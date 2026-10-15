"""Checks that the shipped CAS main dictionary matches its partial sources."""

import json

from plover_korean.tools.dictionary_merger import CAS_MAIN_DICTIONARY, build_cas_main


def test_main_dictionary_is_up_to_date():
    shipped = json.loads(CAS_MAIN_DICTIONARY.read_text(encoding='utf-8'))
    assert shipped == build_cas_main(), \
        'Regenerate with: uv run python -m plover_korean.tools.dictionary_merger'
