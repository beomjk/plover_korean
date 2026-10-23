"""Shared helpers: type Korean CAS strokes through Plover and map them to QWERTY keys."""

import logging

logging.disable(logging.CRITICAL)

from plover import system
from plover.registry import registry
from plover.dictionary.base import load_dictionary
from plover.steno_dictionary import StenoDictionaryCollection
from plover.translation import Translator
from plover.formatting import Formatter
from plover.steno import Stroke, normalize_steno
from plover.config import DEFAULT_UNDO_LEVELS

registry.update()
system.setup("Korean Modern C")
COLLECTION = StenoDictionaryCollection(
    [load_dictionary(p) for p in system.DEFAULT_DICTIONARIES if p.startswith("asset:")])
KEYMAP = system.KEYMAPS["Keyboard"]


class _Output:
    def __init__(self):
        self.text = ""

    def send_backspaces(self, n):
        self.text = self.text[:-n] if n else self.text

    def send_string(self, s):
        self.text += s

    def send_key_combination(self, c):
        self.text += f"<{c}>"

    def send_engine_command(self, c):
        self.text += f"<{c}>"


def type_steno(*strokes):
    """Returns Plover's output for the strokes, without the leading space."""
    out, formatter, translator = _Output(), Formatter(), Translator()
    formatter.set_output(out)
    translator.add_listener(formatter.format)
    translator.set_dictionary(COLLECTION)
    translator.set_min_undo_length(DEFAULT_UNDO_LEVELS)  # as the engine does
    for steno in strokes:
        for part in normalize_steno(steno):
            translator.translate(Stroke(part))
    return out.text.lstrip(" ")


def keys_for(steno):
    """QWERTY keys for one stroke, in keyboard order (left to right, top to bottom)."""
    keys = [KEYMAP[k] for k in Stroke(normalize_steno(steno)[0]).keys()]
    order = "1234567890qwertyuiopasdfghjkl;zxcvbnm,"
    return " ".join(sorted(keys, key=order.index))


def lookup(steno):
    return COLLECTION.lookup(normalize_steno(steno))
