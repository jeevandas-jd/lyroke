import lyricwikia

from lyrics_extractor import SongLyrics
enfine_KEY="AIzaSyCuLw1wg9vLb_CeaAiJnEKGyQmveAA-A1c"

engine_id="c5945596f65464121"

extract_lyrics = SongLyrics(enfine_KEY, engine_id   )

s=extract_lyrics.get_lyrics("shape of you")

print(s)
"""<script async src="https://cse.google.com/cse.js?cx=c5945596f65464121">
</script>
<div class="gcse-search"></div>"""