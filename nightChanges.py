import time
import sys

def type_lyric(line, char_delay=0.065):
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)
    print()

def print_lyrics():
    lyrics = [
        "We're only getting older, baby",
        "And I've been thinking about it lately",
        "Does it ever drive you crazy?",
        "Just how fast the night changes?",
        "Everything that you've ever dreamed of",
        "Disappearing when you wake up",
        "But there's nothing to be afraid of",
        "Even when the night changes",
        "It will never change me and you",
    ]
    delays = [1.6, 1.4, 1.8, 2.1, 2.4, 1.7, 2.0, 2.0, 1.7]

    print("\n🎧 Now Playing: “NIGHT CHANGES” - ONE DIRECTION\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

print_lyrics()
