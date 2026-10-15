"""Checks the particle meta plugins through Plover's translator and formatter."""

import pytest
from plover import system
from plover.formatting import Formatter
from plover.registry import registry
from plover.steno import Stroke, normalize_steno
from plover.steno_dictionary import StenoDictionary, StenoDictionaryCollection
from plover.translation import Translator

DICTIONARY = {
    'ㅎㅈㅏㅣㄱ': '책{^}',
    'ㅅㅏ/ㄱㅗㅏ': '사과{^}',
    '*': '{^ ^}',
    '-ㄹ': '{:ko_particle_reul}',
    'ㅇㅗㅏ': '{:ko_particle_wa}',
    'ㅇㅗㅏㄹ': '{:ko_particle_generic:로}',
}


class Output:
    def __init__(self):
        self.text = ''

    def send_backspaces(self, count):
        self.text = self.text[:-count]

    def send_string(self, text):
        self.text += text

    def send_key_combination(self, combo):
        pass

    def send_engine_command(self, command):
        pass


@pytest.fixture(scope='module', autouse=True)
def korean_system():
    # Loads Plover's built-in metas such as {^} and this plugin's entry points.
    registry.update()
    system.setup('Korean Modern C')


def write(*strokes):
    dictionary = StenoDictionary()
    for steno, translation in DICTIONARY.items():
        dictionary[normalize_steno(steno)] = translation
    output, formatter, translator = Output(), Formatter(), Translator()
    formatter.set_output(output)
    translator.add_listener(formatter.format)
    translator.set_dictionary(StenoDictionaryCollection([dictionary]))
    for steno in strokes:
        translator.translate(Stroke(normalize_steno(steno)[0]))
    return output.text.strip()


@pytest.mark.parametrize('strokes, expected', [
    (['ㅎㅈㅏㅣㄱ', '-ㄹ'], '책을'),
    (['ㅅㅏ', 'ㄱㅗㅏ', '-ㄹ'], '사과를'),
    (['ㅎㅈㅏㅣㄱ', 'ㅇㅗㅏ'], '책과'),
    (['ㅅㅏ', 'ㄱㅗㅏ', 'ㅇㅗㅏ'], '사과와'),
])
def test_particle_follows_previous_word(strokes, expected):
    assert write(*strokes) == expected


@pytest.mark.parametrize('strokes, expected', [
    (['-ㄹ'], '을'),
    (['ㅇㅗㅏ'], '과'),
    (['ㅎㅈㅏㅣㄱ', '*', '-ㄹ'], '책 을'),
])
def test_particle_without_previous_word_uses_consonant_form(strokes, expected):
    assert write(*strokes) == expected


def test_generic_particle_with_bad_rule_outputs_nothing():
    assert write('ㅎㅈㅏㅣㄱ', 'ㅇㅗㅏㄹ') == '책'
