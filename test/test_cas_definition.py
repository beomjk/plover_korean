"""Checks the CAS system definition against Plover's machines."""

import os

from plover.machine.keyboard import Keyboard
from plover.resource import ASSET_SCHEME, resource_exists

from plover_korean.system.cas import definition


def test_default_dictionaries_exist():
    for dictionary in definition.DEFAULT_DICTIONARIES:
        # Plover copies a bare name from DICTIONARIES_ROOT into its config dir.
        if not dictionary.startswith(ASSET_SCHEME):
            dictionary = os.path.join(definition.DICTIONARIES_ROOT, dictionary)
        assert resource_exists(dictionary), dictionary


def test_keyboard_keymap_maps_every_key_once():
    keymap = definition.KEYMAPS['Keyboard']
    bound = [key
             for keys in keymap.values()
             for key in ((keys,) if isinstance(keys, str) else keys)]

    assert set(definition.KEYS) <= set(keymap)
    assert len(bound) == len(set(bound))
    assert set(bound) <= set(Keyboard.get_keys())
