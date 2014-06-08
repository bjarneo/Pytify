import sys
import Spotify as stfy

try:
    if (sys.argv[1]):
        spotify = stfy.Spotify(sys.argv[1])
        spotify.list(15)
except Exception, e:
    print e
    print 'You need to add an argument.\n' \
          'Example python Spotify.py artist or Spotify.py "song name"'