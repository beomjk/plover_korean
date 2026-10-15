"""Checks the CAS system definition against Plover's machines."""

from plover.machine.keyboard import Keyboard

from plover_korean.system.cas import definition


def test_keyboard_keymap_maps_every_key_once():
    keymap = definition.KEYMAPS['Keyboard']
    bound = [key
             for keys in keymap.values()
             for key in ((keys,) if isinstance(keys, str) else keys)]

    assert set(definition.KEYS) <= set(keymap)
    assert len(bound) == len(set(bound))
    assert set(bound) <= set(Keyboard.get_keys())
