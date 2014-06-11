from osascript import osascript, sudo
#osascript('tell application "Spotify" to artist of current track as string')
print osascript('tell application "spotify" to next track')