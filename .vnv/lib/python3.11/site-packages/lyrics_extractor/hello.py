from lyrics.lyrics_extractor import Song_Lyrics


GCS_API_KEY = "AIzaSyDXM0_uug2UyrxlJrCM2gqnAwHWdwV6F0o"
GCS_ENGINE_ID = "014644109399637185726:udob-f3brnc"

extract_lyrics = Song_Lyrics(GCS_API_KEY, GCS_ENGINE_ID)
song_title, song_lyrics = extract_lyrics.get_lyrics("Har ghadi")
