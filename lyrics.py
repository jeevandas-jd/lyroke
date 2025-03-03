import lyricsgenius as lg
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("GENIUS_API_TOKEN")

if not api_key:
    print("API token not found. Please check your .env file.")
    exit()


genius = lg.Genius(api_key)

while True:
    input_artist = input("Enter the name of the artist: ")

    # Search for the artist and get up to 5 songs
    artist = genius.search_artist(input_artist, max_songs=5)

    if artist:
        songs = artist.songs

        # Display the list of songs
        for i, song in enumerate(songs):
            print(f"{i + 1}. {song.title}")

        # Ask if the user wants to see lyrics
        is_lyrics = input("Do you want to see the lyrics of any of these songs? (y/n): ")

        if is_lyrics.lower() == 'y':
            try:
                song_number = int(input("Enter the song number: "))
                if 1 <= song_number <= len(songs):
                    print(f"\nLyrics of {songs[song_number - 1].title}:\n")
                    print(songs[song_number - 1].lyrics)
                else:
                    print("Invalid song number.")
            except ValueError:
                print("Please enter a valid number.")

        else:
            print("Thank you for using this program!")
    else:
        print(f"No results found for artist: {input_artist}")

    # Ask if the user wants to search for another artist
    ask = input("Do you want to search for another artist? (y/n): ")
    if ask.lower() == 'n':
        print("Goodbye!")
        break
