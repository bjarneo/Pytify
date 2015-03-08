Spotipy
=============

Search and start songs from command line.<br>
Should work in Linux and OS X.<br>
Supports both python 2 and 3. <br>

![Image of terminal]
(http://i.imgur.com/EpUDMJo.gif)

### Dependency
```bash
pip install requests
```

### Usage
```python
# To start the app type
./cli.py

# next song
./cli.py -n

# prev song
./cli.py -p

# play and pause song
./cli.py -pp
```

```python
# To symlink this app so you don't need to write python cli.py or ./cli.py do this:
sudo ln -s ~/Path/To/cli.py  /usr/local/bin/spotipy
```

#### Usage is now
```python
# To start the app type
spotipy

# next song
spotipy -n

# prev song
spotipy -p

# play and pause song
spotipy -pp

```

### Contributing
Contributions are appreciated.

### Contributors
- [@joined](https://github.com/joined/) - OS X
- [@adam410](https://github.com/adam410/) - OS X issue
- [@Newky](https://github.com/Newky) - Better structure
- [@ymski](https://github.com/ymski) - OS X 
