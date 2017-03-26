# [spockpy](http://spockpy.readthedocs.io)
> *"A Python hand gesture recognition library for Kinetic User Interface (KUI)."*

[![Documentation Status](https://readthedocs.org/projects/spockpy/badge/?version=latest)](http://spockpy.readthedocs.io/en/latest/?badge=latest) [![Python](https://img.shields.io/badge/python-2.7, 3.5-blue.svg)]() [![License](https://img.shields.io/badge/license-Apache 2.0-blue.svg)](LICENSE) [![Say Thanks](https://img.shields.io/badge/Say Thanks-!-blue.svg)]()

![](.github/logo.png)

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [License](#license)

### Installation
##### 1. Download the repository

Clone the base repository onto your desktop with `git` as follows:
```console
$ git clone git@github.com:achillesrasquinha/spockpy
```

##### 2. Install necessary dependencies
spockpy is primarily built on [OpenCV](http://opencv.org) for a large number of standard Computer Vision helpers and techniques. In order to install spockpy, you may have to build OpenCV (2.x or 3.x, depending on your Python version) first.

For Linux users, use our build scripts as follows:
```console
$ chnmod +x build/*
$ build/get-opencv.sh
```

Next, install necessary Python dependencies as follows:
```console
$ pip install -r requirements.txt
```

Finally, go ahead and install spockpy onto your system.
```console
$ python setup.py install
```

To check whether you've installed spockpy, simply `import` spockpy:
```python
>>> import spockpy
```

Come this far? You have my [Vulcan Salute!](https://en.wikipedia.org/wiki/Vulcan_salute)

![](.github/live-long-and-prosper.jpg)

### Usage
spockpy creates a virtual trackpad (we call this, a *HoverPad*) for your user to interact with the API. Create a `spockpy.HoverPad` object as follows:
```python
>>> import spockpy
>>> pad = spockpy.HoverPad(verbose = True)
```

To display the `HoverPad`, use the `show` class method as follows:
```python
>>> pad.show()
```

### How about Rock?
![](.github/spockpy-rock.png)

### What about Paper?
![](.github/spockpy-paper.png)

### Also, maybe Spock?
![](.github/spockpy-spock.png)

`spockpy.HoverPad` releases a set of event objects from the `event` class method

### Examples
spockpy comes with a handy number of examples.
To launch the app, launch it as follows:
```python
>>> import spockpy
>>> app = spockpy.App()
>>> app.run()
```
OR via the command-line
```console
$ python -m spockpy
```

![](.github/spockpy-win.png)
![](.github/spockpy-lose.png)
![](.github/spockpy-tie.png)

###

### License
This repository has been released under the [Apache License 2.0](LICENSE)
