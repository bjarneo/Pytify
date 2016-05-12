Pytify
=============

[![Code Climate](https://codeclimate.com/github/bjarneo/Pytify/badges/gpa.svg)](https://codeclimate.com/github/bjarneo/Pytify)

Search and start songs from the CLI.
Linux and OS X support.

Python 3 support. For Python 2 support use this release: [v2.1.0](https://github.com/bjarneo/Pytify/tree/v2.1.0)

![Image of terminal]
(http://i.imgur.com/I1uvoVx.gif)


## Installation
```bash
$ sudo pip install pytify
```

## Features
* Auto suggest (based on history)
* Search history
* Search and play songs
* CLI commands
* VIM navigation bindings

## Clone repo
```bash
$ git clone https://github.com/bjarneo/pytify.git
$ cd pytify
$ sudo python setup.py install
```

### Usage
```bash
# To start the app type
$ pytify

# next song
$ pytify -n

# prev song
$ pytify -p

# play and pause song
$ pytify -pp
```

### Dependency
```bash
* requests
* prompt-toolkit
```

### Contributing
Contributions are appreciated.

### Contributors
- [@joined](https://github.com/joined/) - OS X
- [@adam410](https://github.com/adam410/) - OS X issue
- [@Newky](https://github.com/Newky) - Better structure
- [@ymski](https://github.com/ymski) - OS X
- [@wohlfea](https://github.com/wohlfea) - Made it compatible with python 3.5
- [@ddiddi](https://github.com/ddiddi) - Added search phrase history browsing. (auto complete)
