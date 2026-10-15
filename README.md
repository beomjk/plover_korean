# Plover Korean

Korean stenography for [Plover](https://github.com/openstenoproject/plover).

- [Korean Modern C - CAS-based System](#korean-modern-c)
- [Korean Modern S - Sorizava-based System](#korean-modern-s)
- [Meta Plugins](#meta-plugins)

## Installation

*This plugin has not been released on PyPI yet, so locally installing from source is currently the only option*

The macOS Plover app cannot build packages from source, since pip re-runs `sys.executable` for build steps and in the app that is the Plover launcher. Build a wheel with [uv](https://docs.astral.sh/uv/) instead and install that file:

```sh
# Editable: Plover runs the code in this folder, so edits only need a Plover restart.
uv run python -c "from setuptools import build_meta; print(build_meta.build_editable('dist'))"
/Applications/Plover.app/Contents/MacOS/Plover -s plover_plugins install dist/plover_korean-0.0.3-0.editable-py3-none-any.whl
```

Rebuild and reinstall only when `pyproject.toml` changes (dependencies or entry points). For a regular install, install the wheel from `uv build --wheel` instead.

If you have issues with character misalignment in places like the Paper Tape in the Plover GUI try installing [Nanum Gothic Coding](https://fonts.google.com/earlyaccess#Nanum+Gothic+Coding), a monospaced sans-serif Korean font, and setting Plover's font to that where possible. The majority of monospaced fonts do not have CJK language support which is why this issue comes up for things relying on monospaced plain text display.

## Korean Modern C

![CAS Layout](https://i.imgur.com/T9Kfc07.png)

Korean Modern C is a Korean stenography system based on the system used by Korean CAS machines. See the reference guide for this system [here](/plover_korean/system/cas/docs/README.md).

### Keyboard Layout

The default keymap is for a regular QWERTY keyboard, with the vowels under the thumbs like English steno's `c v | n m`:

| Row | Left hand | Right hand |
| --- | --- | --- |
| Numbers | `1 2 3 4 5` | `6 7 8 9 0` |
| Top | `q w e r t` = ㅎ ㅁ ㄱ ㅈ ㄴ | `y u i o p` = ㅎ ㅇ ㄹ ㄱ ㄷ |
| Home | `a s d f g` = ㄷ ㅇ ㅅ ㅂ ㄹ | `h j k l ;` = ㅂ ㄴ ㅅ ㅈ ㅁ |
| Thumbs | `x c v` = ㅗ ㅏ ㅜ | `b n m` = * ㅓ ㅣ |

### Dictionaries

- `ko_user.json`: your own entries. Plover copies it into its config folder once, and Add Translation saves to it.
- `ko_cas_main.json`: briefs, particles, conjugations, symbols and commands. It is generated from `plover_korean/system/cas/dictionaries/partial/`; run `uv run python -m plover_korean.tools.dictionary_merger` after editing those files.
- `ko_cas_numbers.py` and `ko_cas_base.py`: numbers and syllable blocks, built in code.

The last three are read straight from the installed plugin, so they update along with it.

### Commands

All commands start with `ㅎㅂㄹㅗ` ("플로" as in Plover). To change one, add your own stroke to `ko_user.json`.

| Stroke | Keyboard | Command |
| --- | --- | --- |
| `ㅎㅂㄹㅗ` | `q f g x` | Toggle Plover output |
| `ㅎㅂㄹㅗㅇ` | `q f g x u` | Switch to English Stenotype |
| `ㅎㅂㄹㅗㄷ` | `q f g x p` | Add translation |
| `ㅎㅂㄹㅗㅅ` | `q f g x k` | Lookup |

## Korean Modern S

![Sorizava Layout](https://i.imgur.com/kpEL3mE.png)

Korean Modern S is a Korean stenography system based on the system used by Sorizava machines. See the reference guide for this system [here](/plover_korean/system/sorizava/docs/README.md).

## Meta Plugins

In order to use these meta plugins you need to add them with a dictionary entry like the example below:

``` json
{
    "ㄴㅣㄱ": "{:meta_plugin_name:meta_plugin_argument1,meta_plugin_argument2,...}"
}
```

If there are no arguments for the meta plugin, just `{:meta_plugin_name}` is sufficient.

### Particles

Regex support for Korean syllable blocks does not work well so various meta plugins have been created for contextually determining what particle to attach to a word.

While many particles are always the same when attached to words, some change their form depending on if the word they are attached to ends with a vowel or consonant. The following table lists the current plugins with that support that can be used:

Meta Plugin Name | Concept
---------------- | ----------
ko_particle_neun | ~는/은
ko_particle_ga   | ~가/이
ko_particle_reul | ~를/을
ko_particle_da   | ~다/이다
ko_particle_ra   | ~라/이라
ko_particle_ya   | ~야/아
ko_particle_wa   | ~와/과
ko_particle_rang | ~랑/이랑
ko_particle_na   | ~나/이나
ko_particle_ro   | ~로/으로
ko_particle_myeo | ~며/이며

If support for a particular variable particle is not currently implemented, [**please open an issue on GitHub for support to be added**](https://github.com/nsmarkop/plover_korean/issues). However, there is one additional meta plugin that can be used for when this occurs: "ko_particle_generic". It has three plugin arguments:

1. The particle to be used for words ending in vowels.
2. The particle to be used for words ending in consonants.
3. (optional) The final consonant of words where the consonant case should be treated as the vowel case.

For example, an entry that replicates the "ko_particle_neun" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:는,은}"
}
```

An entry that replicates the "ko_particle_ro" functionality would be:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:로,으로,ㄹ}"
}
```

If you attempt to use these plugins to attach particles to non-Korean words they cannot accurately determine how to display and will fall back to a default case.

## License

GPLv3+.
