PythonSpotify
=============

Search and start songs from command line.<br>

![Image of terminal]
(http://i57.tinypic.com/2i0ver4.png)

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
# For symlink this app, add it to usr local bin. Example:
sudo ln -s ~/Path/To/cli.py  /usr/local/bin/song
```

#### Usage is now
```python
# To start the app type
song

# next song
song -n

# prev song
song -p

# play and pause song
song -pp

```