import Spotify as stfy

print 'What are you searching for?'
search_input = raw_input()

try:
    if (search_input):
        spotify = stfy.Spotify(search_input)
        spotify.list(15)
except Exception, e:
    print e
    print """
    You need to add an argument.
    Example python Spotify.py artist or Spotify.py 'song name'
    """