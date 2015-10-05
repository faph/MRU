![Travis](https://img.shields.io/travis/faph/MRU.svg?style=flat-square)
![Coveralls](https://img.shields.io/coveralls/faph/MRU.svg?style=flat-square)
[![Conda](https://anaconda.org/faph/mru/badges/installer/conda.svg)](https://anaconda.org/faph/mru)
[![PyPI](https://img.shields.io/pypi/v/mru.svg?style=flat-square)](https://pypi.python.org/pypi/mru)

# MRU

Small Python module to manage Most Recently Used (MRU) file paths.

Say you want to remember the most recently used files so the user can quickly select one of these next time the
application is launched. This module will manage that for you:

```python
>>> from mru import MRU
>>> history = MRU(app='Economy App', org='Balliol College')
>>> history.add('~/Documents/Intro.pdf')
>>> pass  # ...later...
>>> history.add('~/Documents/The Wealth of Nations.pdf')
>>> history[0]
'~/Documents/The Wealth of Nations.pdf'
```

Entries are automatically saved to disk, so opening the application again works as aspected:

```python
>>> from mru import MRU
>>> history = MRU(app='Economy App', org='Balliol College')
>>> list(history)
['~/Documents/The Wealth of Nations.pdf', '~/Documents/Intro.pdf']
```

`MRU` instances are iterables (`collections.deque`, more precisely). So you can iterate over the object directly,
convert to lists etc. The most recent item comes first:

>>> for path in history:
...     print(path)
...
~/Documents/The Wealth of Nations.pdf
~/Documents/Intro.pdf

By default, `MRU` remembers up to 20 paths. Change this like this:

```python
>>> history = MRU(app='Economy App', org='Balliol College', maxlen=10)
```

To remove all entries:

```python
>>> history.clear()
>>> list(history)
[]
```

Where are the file paths saved? Depending on the platform, somewhere in the user's profile. For example on Windows:
`C:\Users\Adam Smith\AppData\Local\Balliol College\Economy App\mru`.

MRU uses the [AppDirs module](https://github.com/ActiveState/appdirs) to find a suitable location using
`user_config_dir(app, org)`.

## Licence

Distributed under the [MIT licence](LICENSE).
