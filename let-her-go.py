import time
import sys

def type_lyric(line, char_delay=0.065):
    # Set flush=True to ensure immediate printing character by character
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "Well you only need the light when it's burning low",
        "Only miss the sun when it starts to snow",
        "Only know you love her when you let her go", # The first hook is critical
        "Only know you've been high when you're feeling low",
        "Only hate the road when you're missing home",
        "Only know you love her when you let her go", # The main hook
        "And you let her go...",
    ]
    
    # REVISED Timings (in seconds) for a slower, more emotional feel
    # I increased the delay on the third and sixth lines to emphasize the main message.
    delays = [2.5, 2.3, 3.5, 2.5, 2.3, 3.5, 5.0] 

    print("\n🎧 Now Playing: “LET HER GO” - PASSENGER\n")
    time.sleep(1.5)

    # Loop through the lyrics and display them
    for i, line in enumerate(lyrics):
        type_lyric(line)
        # Pause for the specified duration before the next line
        if i < len(delays):
            time.sleep(delays[i])

# Start the process
print_lyrics()
