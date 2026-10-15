"""Stenography definition for Korean based on the 36-key CAS layout."""

from typing import Tuple, Dict, List, Optional


# Consonant groups don't internally follow a steno order when constructing words.
KEYS: Tuple[str] = (
    '1-', '2-', '3-', '4-', '5-',
    # 초성 - Initial consonant
    'ㅎ-', 'ㅁ-', 'ㄱ-', 'ㅈ-', 'ㄴ-',
    'ㄷ-', 'ㅇ-', 'ㅅ-', 'ㅂ-', 'ㄹ-',

    # 중성 - Medial vowel
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-*', '-ㅓ', '-ㅣ',

    '-6', '-7', '-8', '-9', '-0',
    # 종성 - Final consonant
    '-ㅎ', '-ㅇ', '-ㄹ', '-ㄱ', '-ㄷ',
    '-ㅂ', '-ㄴ', '-ㅅ', '-ㅈ', '-ㅁ'
)

IMPLICIT_HYPHEN_KEYS: Tuple[str] = (
    'ㅗ-', 'ㅏ-', 'ㅜ-',
    '-*', '-ㅓ', '-ㅣ'
)

SUFFIX_KEYS: Tuple[str] = ()

# This system has explicit number keys, so there is no need for these.
NUMBER_KEY: str = None
NUMBERS: Dict[str, str] = {}

# Can be overridden or alternatives can be made in a dictionary.
UNDO_STROKE_STENO: str = '-ㅂㄴ'

ORTHOGRAPHY_RULES: List[Tuple[str, str]] = []
ORTHOGRAPHY_RULES_ALIASES: Dict[str, str] = {}
ORTHOGRAPHY_WORDLIST: Optional[str] = None

KEYMAPS: Dict[str, Dict[str, Tuple[str]]] = {
    # Mapped for a regular QWERTY keyboard, with the vowels on x c v | b n m
    # for the thumbs like English steno's c v | n m. A CAS keyboard's QWERTY
    # layer instead puts the vowels on z x c | v b n and -ㅁ on m.
    'Keyboard': {
        '1-': '1',
        '2-': '2',
        '3-': '3',
        '4-': '4',
        '5-': '5',

        'ㅎ-': 'q',
        'ㅁ-': 'w',
        'ㄱ-': 'e',
        'ㅈ-': 'r',
        'ㄴ-': 't',

        'ㄷ-': 'a',
        'ㅇ-': 's',
        'ㅅ-': 'd',
        'ㅂ-': 'f',
        'ㄹ-': 'g',

        'ㅗ-': 'x',
        'ㅏ-': 'c',
        'ㅜ-': 'v',

        '-*': 'b',
        '-ㅓ': 'n',
        '-ㅣ': 'm',

        '-6': '6',
        '-7': '7',
        '-8': '8',
        '-9': '9',
        '-0': '0',

        '-ㅎ': 'y',
        '-ㅇ': 'u',
        '-ㄹ': 'i',
        '-ㄱ': 'o',
        '-ㄷ': 'p',

        '-ㅂ': 'h',
        '-ㄴ': 'j',
        '-ㅅ': 'k',
        '-ㅈ': 'l',
        '-ㅁ': ';',

        'arpeggiate': 'space',
        'no-op': ()
    }
}

DICTIONARIES_ROOT: str = 'asset:plover_korean:system/cas/dictionaries'
DEFAULT_DICTIONARIES: List[str] = [
    # Generated from partial/ by plover_korean.tools.dictionary_merger.
    'ko_cas_main.json',
    'ko_cas_numbers.py',
    'ko_cas_base.py'
]
