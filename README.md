Pytify
=============

[![Code Climate](https://codeclimate.com/github/bjarneo/Pytify/badges/gpa.svg)](https://codeclimate.com/github/bjarneo/Pytify)

Search and start songs from the CLI.  
Linux and OS X support.

*Spotify must be running in the background in order to use this cli remote*

<img src="logo.png" align="right" />

Python 3 support. For Python 2 support use this release: [v2.1.0](https://github.com/bjarneo/Pytify/tree/v2.1.0)

![Image of terminal](http://i.imgur.com/P6Qsp8I.gif)


## Installation
```bash
$ sudo pip install pytify
```

Linux you need to install `python-dbus` package.
```bash
$ # Example using apt-get
$ apt-get install python-dbus
```

## Features
* Commands
* Auto suggest (based on history)
* Tab through history
* Search history
* Search and play songs
* CLI commands
* VIM navigation bindings

## Clone repo
```bash
$ git clone https://github.com/bjarneo/Pytify.git
$ cd Pytify
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

# Current playing song
$ pytify -c
```

Commands  
![commands](http://i.imgur.com/r7pCYyH.png)
```
Commands:
 current              print current song
 help                 list all commands
 next                 play next song
 pp                   play or pause song
 stop                 stop
 prev                 play previous song
 history              last five search results

```

### Install dev dependencies
pip version must be > 9
```bash
$ pip install -r requirements.txt
```

### Dependencies
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
- [@kmatt](https://github.com/kmatt) - Minor UX changes
