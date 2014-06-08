import requests
import time

# Fetch songs with spotify api
class Spotify:
  _url = 'https://ws.spotify.com/search/1/track.json?q='

  # Get our data
  def __init__(self, query):
    response = requests.get(self._url + query)
    self.data = response.json()
  
  # List all. Limit if needed
  def list(self, limit = 100):
    for key, song in enumerate(self.data['tracks']):
      if (key == limit):
        break

      print str(key + 1) + '. ' + song['artists'][0]['name'] + ' - ' + song['name'] + ' :: ' + song['album']['name']
      # Sleeps just for the sexy output
      time.sleep(0.03) 
      
  # Debug
  def debug(self):
    print self.data['tracks']