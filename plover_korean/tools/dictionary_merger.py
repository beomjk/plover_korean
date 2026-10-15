'''
Builds the CAS main dictionary from the hand-edited partial dictionaries.

Run this after editing anything in system/cas/dictionaries/partial:

    uv run python -m plover_korean.tools.dictionary_merger
'''

import json
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from plover import system
from plover.registry import registry
from plover.steno import normalize_steno

from plover_korean.system.cas import definition as cas_definition
from plover_korean.tools.utilities import create_plover_dictionary


CAS_SYSTEM_NAME = 'Korean Modern C'
CAS_DICTIONARIES_DIR = Path(__file__).resolve().parent.parent / 'system' / 'cas' / 'dictionaries'
CAS_PARTIAL_DIR = CAS_DICTIONARIES_DIR / 'partial'
CAS_MAIN_DICTIONARY = CAS_DICTIONARIES_DIR / 'ko_cas_main.json'


def load_partial(path: Path) -> List[Tuple[str, str]]:
    '''
    Returns (stroke, translation) pairs from a partial dictionary.

    YAML partials map each translation to a list of strokes, while JSON
    partials use Plover's own stroke to translation format.
    '''

    text = path.read_text(encoding='utf-8')
    if path.suffix == '.yaml':
        return [(stroke, translation)
                for translation, strokes in yaml.safe_load(text).items()
                for stroke in strokes]
    return list(json.loads(text).items())


def build_cas_main() -> Dict[str, str]:
    '''
    Merges every CAS partial dictionary, with strokes normalized the way
    Plover will read them. Fails on strokes Plover cannot parse and on a
    stroke given different translations.
    '''

    registry.register_plugin('system', CAS_SYSTEM_NAME, cas_definition)
    system.setup(CAS_SYSTEM_NAME)

    merged: Dict[str, str] = {}
    sources: Dict[str, str] = {}
    partials = sorted(CAS_PARTIAL_DIR.glob('*.yaml')) + sorted(CAS_PARTIAL_DIR.glob('*.json'))
    for path in partials:
        for raw_stroke, translation in load_partial(path):
            try:
                stroke = '/'.join(normalize_steno(raw_stroke))
            except ValueError as error:
                raise ValueError(f'{path.name}: {raw_stroke!r} ({translation!r}): {error}') from error
            if merged.get(stroke, translation) != translation:
                raise ValueError(f'{stroke!r} is {merged[stroke]!r} in {sources[stroke]} '
                                 f'but {translation!r} in {path.name}')
            merged[stroke] = translation
            sources[stroke] = path.name
    return merged


if __name__ == '__main__':
    create_plover_dictionary(CAS_MAIN_DICTIONARY, build_cas_main())
