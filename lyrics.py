import lyricsgenius as lg

genius =lg.Genius("ecgGNpmLy4EXajEKfSuFRfC4dtLeT3fXCScRqJCazw1W2W2rVW9zDJDSydKUcbew")
while True:
    input_artist=input("Enter the name of the artist: ")

    artist = genius.search_artist(input_artist, max_songs=5)

    songs = artist.songs
    for i, song in enumerate(songs):
        print(f"{i+1}. {song.title}")

    is_lyrics = input("Do you want to see the lyrics of any of these songs? (y/n): ")

    if is_lyrics == 'y':
        song_number = int(input("Enter the song number: "))
        print(songs[song_number-1].lyrics)
    else:    
        print("Thank you for using this program!")
    ask=input("Do you want to search for another artist? (y/n): ")
    if ask=='n':
        break
    else:
        continue