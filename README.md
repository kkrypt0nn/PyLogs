# PyLogs
PyLogs is a python library made by Krypton so that it is easier for everyone to add logs into their python projects.

## Getting Started
By following the incoming instructions, you will be able to get PyLogs into any of your projects.

### Prerequisites
To be able to use PyLogs you will need:
- Python 3.x

### Installing
- Clone or download this github repository

```
git clone https://github.com/kkrypt0nn/PyLogs.git
```

- Move all the files into your folder where your python project is
- To start using PyLogs you need to import the `Logger.py` file

```python
import PyLogs

print(PyLogs.__name__ + ", Version " + PyLogs.__version__)
print("Made by " + PyLogs.__author__)
```

- To create new logs you will need to import the class `Log` from `Loggger.py`

```python
import PyLogs
from PyLogs import Log

print(PyLogs.__name__ + ", Version " + PyLogs.__version__)
print("Made by " + PyLogs.__author__ + "\n\n")

# Prints Critical Error Message With Color
Log.critical("Critical Error Message", True)
# Prints Critical Error Message Without Color
Log.critical("Critical Error Message", False)

# Prints Warning Message With Color
Log.warning("Warning Message", True)
# Prints Warning Message Without Color
Log.warning("Warning Message", False)
```

If you still do not understand after following these steps, there is an example file called [Example.py](Example.py).

## Built With
- [PyCharm](https://jetbrains.com/pycharm/download)
- [Python 3.x](https://python.org/downloads)

## Contributing
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to this project.

## Bugs & TODOs
The list of known bugs of PyLogs is available [here](BUGS.md).

The TODO list of PyLogs is available [here](TODOS.md).

## Issues
Before submitting any issues, make sure to read the [known bugs](BUGS.md) file.

Submit your issues that you encounter while installing and using PyLogs [here](https://github.com/kkrypt0nn/PyLogs/issues).

## Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/kkrypt0nn/PyLogs/tags).

## Authors
- **Krypton** - *Initial work* - [kkrypt0nn](https://github.com/kkrypt0nn)

## License
This project is licensed under the [Apache 2.0](LICENSE.md) License - see the [LICENSE.md](LICENSE.md) file for details.