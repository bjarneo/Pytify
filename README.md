PythonSpotify
=============

Search and start songs from command line.<br>

![Image of terminal]
(http://i.imgur.com/B7t7gdh.gif)

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
