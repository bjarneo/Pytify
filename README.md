Pytify
=============

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4JDQMB6MRJXQE&source=url)
[![Code Climate](https://codeclimate.com/github/bjarneo/Pytify/badges/gpa.svg)](https://codeclimate.com/github/bjarneo/Pytify)

![Pytify logo](https://github.com/bjarneo/Pytify/blob/master/logo.png?raw=true)

Search and start songs from the CLI.  
Linux and OS X support.

*Spotify must be running in the background in order to use this cli remote*

Python 3 support. For Python 2 support use this release: [v2.1.0](https://github.com/bjarneo/Pytify/tree/v2.1.0)

![Image of terminal](http://i.imgur.com/P6Qsp8I.gif)


## Installation
```bash
$ pip install pytify
```

Python 2
```bash
$ pip install pytify==2.1.0
```

Linux you need to install `python-dbus` package.
```bash
$ # Example using apt-get
$ apt-get install python-dbus
```

## Credentials
This package now must use credentials in order to search for songs. 

Support for client credentials flow. Please follow these steps:

1. Register app: https://developer.spotify.com/my-applications/#!/applications
2. Edit your `~/.bashrc` to export following values:
```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
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
- [@bharath123](https://github.com/bharath-123) - Updated Pytify to use prompt_toolkit v2
- .... and other.. please add your name and code update!

### Logo
Logo by [theodorosploumis](https://github.com/theodorosploumis). Thank you very much!

## Donation
If this project has been helpful in any way, and you want to treat me a cup of coffee, please donate :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=4JDQMB6MRJXQE&source=url)
