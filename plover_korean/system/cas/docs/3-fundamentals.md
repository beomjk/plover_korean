# Fundamentals

Before getting into the theory, here are a few things you should know.

## Spacing

In this system you usually add spaces yourself: the `*` key on its own types a space. Adding a space after every stroke, as English steno does, does not suit this theory, because it is built on syllable blocks rather than words. Once you start using particles and other briefs, though, you can rely on automatic spacing more.

In the [Korean plugin](https://github.com/nsmarkop/plover_korean) for [Plover](https://github.com/openstenoproject/plover), this means a dictionary entry that should attach to what follows must end with the attach operator `{^}`. An entry that does not end with `{^}` is treated as ending a word, so a space follows it. These notes show the attach operator wherever an entry has one.

Keep this in mind when you add entries to your own dictionary.

## Suppressing Spaces

Sometimes a space appears where you don't want one. Plover's [dictionary format wiki page](https://github.com/openstenoproject/plover/wiki/Dictionary-Format) describes the syntax you can use in dictionary entries to prevent this. TODO: add a stroke like D-LS to the default dictionary to go with `*`.

## Undo

To undo what you just typed, use the `-ㅂㄴ` stroke.