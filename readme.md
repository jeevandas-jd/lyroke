Lyroke 🎶
Lyroke is a work-in-progress project aiming to build a music recognition and lyrics extraction system. The final goal is to create a CLI-based lyrical video, where a song plays in the background and synced lyrics appear on the command line with minimal latency.

This project is currently read-only and under development.

How It Works (For Now)
Fetches lyrics using the Genius API.
Lets you browse an artist’s songs and view their lyrics in the CLI.
Setup
Install dependencies:
bash
Copy
Edit
pip install lyricsgenius python-dotenv
Add your Genius API key to a .env file:
ini
Copy
Edit
GENIUS_API_TOKEN=your-genius-api-key
Run the script:
bash
Copy
Edit
python lyroke.py
Future Plans
Music recognition from audio.
Real-time lyric syncing with background music.