# Plover Korean

Korean stenography for [Plover](https://github.com/openstenoproject/plover).

- [Korean Modern C - CAS-based System](#korean-modern-c)
- [Korean Modern S - Sorizava-based System](#korean-modern-s)
- [Meta Plugins](#meta-plugins)

## Installation

*This plugin is not on PyPI yet, so the only way to install it is from source.*

The macOS Plover app cannot build a package from source: pip runs build steps with `sys.executable`, which inside the app is the Plover launcher. Instead, build a wheel with [uv](https://docs.astral.sh/uv/) and install that:

```sh
# Editable install: Plover runs the code in this folder, so after editing it you only need to restart Plover.
uv run python -c "from setuptools import build_meta; print(build_meta.build_editable('dist'))"
/Applications/Plover.app/Contents/MacOS/Plover -s plover_plugins install dist/plover_korean-0.0.3-0.editable-py3-none-any.whl
```

You only need to rebuild and reinstall when `pyproject.toml` changes (dependencies or entry points). For a regular, non-editable install, use the wheel from `uv build --wheel` instead.

If Korean text looks misaligned in monospaced views such as the Paper Tape, install [Nanum Gothic Coding](https://fonts.google.com/earlyaccess#Nanum+Gothic+Coding), a monospaced sans-serif Korean font, and select it in Plover's font settings where you can. Most monospaced fonts do not support Korean, which causes the misalignment.

## Korean Modern C

![CAS Layout](https://i.imgur.com/T9Kfc07.png)

Korean Modern C is based on the stenography system used by Korean CAS machines. See the [reference guide](/plover_korean/system/cas/docs/README.md) for its theory.

For a step-by-step tutorial in Korean on learning it with a regular keyboard, see [docs/tutorial](/docs/tutorial/README.md). `docs/tutorial/tools/build_tutorial.py` generates its examples by typing each one through Plover, and a test fails when the committed pages fall out of date. After changing the keymap or dictionaries, regenerate them with `uv run python docs/tutorial/tools/build_tutorial.py`.

### Keyboard Layout

The default keymap targets a regular QWERTY keyboard. The vowels sit under the thumbs, around the `c v | n m` keys that English steno uses for its vowels:

| Row | Left hand | Right hand |
| --- | --- | --- |
| Numbers | `1 2 3 4 5` | `6 7 8 9 0` |
| Top | `q w e r t` = ㅎ ㅁ ㄱ ㅈ ㄴ | `y u i o p` = ㅎ ㅇ ㄹ ㄱ ㄷ |
| Home | `a s d f g` = ㄷ ㅇ ㅅ ㅂ ㄹ | `h j k l ;` = ㅂ ㄴ ㅅ ㅈ ㅁ |
| Thumbs | `x c v` = ㅗ ㅏ ㅜ | `b n m` = * ㅓ ㅣ |

### Dictionaries

- `ko_user.json`: your own entries. Plover copies it into its config folder the first time, and Add Translation saves new entries there.
- `ko_cas_main.json`: briefs, particles, conjugations, symbols and commands. It is generated from `plover_korean/system/cas/dictionaries/partial/`; run `uv run python -m plover_korean.tools.dictionary_merger` after editing those files.
- `ko_cas_numbers.py` and `ko_cas_base.py`: numbers and syllable blocks, generated in code.

Plover reads the last three directly from the installed plugin, so they stay current when the plugin is updated.

### Commands

Every command stroke starts with `ㅎㅂㄹㅗ` ("플로", as in Plover). To use a different stroke, add your own entry to `ko_user.json`.

| Stroke | Keyboard | Command |
| --- | --- | --- |
| `ㅎㅂㄹㅗ` | `q f g x` | Toggle Plover output |
| `ㅎㅂㄹㅗㅇ` | `q f g x u` | Switch to English Stenotype |
| `ㅎㅂㄹㅗㄷ` | `q f g x p` | Add translation |
| `ㅎㅂㄹㅗㅅ` | `q f g x k` | Lookup |

## Korean Modern S

![Sorizava Layout](https://i.imgur.com/kpEL3mE.png)

Korean Modern S is based on the stenography system used by Sorizava machines. See its [reference guide](/plover_korean/system/sorizava/docs/README.md).

## Meta Plugins

To use a meta plugin, add a dictionary entry like this:

``` json
{
    "ㄴㅣㄱ": "{:meta_plugin_name:meta_plugin_argument1,meta_plugin_argument2,...}"
}
```

If the meta plugin takes no arguments, `{:meta_plugin_name}` is enough.

### Particles

Regular expressions do not work well with Korean syllable blocks, so these meta plugins choose the particle from the word before it instead.

Most particles never change, but some take a different form depending on whether the word before them ends in a vowel or a consonant. These meta plugins handle those particles:

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

If a particle you need is missing, [**please open an issue on GitHub**](https://github.com/nsmarkop/plover_korean/issues). In the meantime, you can use the `ko_particle_generic` meta plugin, which takes three arguments:

1. The particle to use after a vowel.
2. The particle to use after a consonant.
3. (Optional) A final consonant after which the vowel form is used instead.

For example, this entry works the same as `ko_particle_neun`:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:는,은}"
}
```

And this one works the same as `ko_particle_ro`:

``` json
{
    "ㄴㅣㄱ": "{:ko_particle_generic:로,으로,ㄹ}"
}
```

After a word that is not Korean, these plugins cannot tell which form is correct and fall back to a default.

## License

GPLv3+.
