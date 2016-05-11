Pytify
=============

Search and start songs from command line.<br>
Should work in Linux and OS X.<br>
Supports both python 2 and 3. <br>

![Image of terminal]
(http://i.imgur.com/zlt3f8P.gif)


## Installation
```python
$ sudo pip install pytify
```

## Or clone the repo
```python
$ git clone https://github.com/bjarneo/pytify.git
$ cd pytify
$ sudo python setup.py install
```

### Usage
```python
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
pip install requests gnureadline
```

### Contributing
Contributions are appreciated.

### Contributors
- [@joined](https://github.com/joined/) - OS X
- [@adam410](https://github.com/adam410/) - OS X issue
- [@Newky](https://github.com/Newky) - Better structure
- [@ymski](https://github.com/ymski) - OS X
- [@wohlfea](https://github.com/wohlfea) - Make it compatible with python 3.5
- [@ddiddi](https://github.com/ddiddi) - Added search phrase history browsing. (auto complete)
