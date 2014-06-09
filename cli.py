#!/usr//bin/env python
import Spotify


search_input = raw_input('What artist / song are you searching for?\n')

if search_input:
    spotify = Spotify.Spotify(search_input)
    spotify.list(10)
else:
    print """
    You need to add an argument.
    """