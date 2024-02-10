import yt_dlp

URL = 'https://www.youtube.com/watch?v=wtolixa9XTg'

with yt_dlp.YoutubeDL() as ydl:
    info = ydl.extract_info(URL, download=False)
for format in info["formats"][::-1]:
    if format["resolution"] == "audio only" and format["ext"] == "m4a":
        url = format["url"]
        break
        
print(url)
import assemblyai as aai

# If the API key is not set as an environment variable named
# ASSEMBLYAI_API_KEY, you can also set it like this:
# aai.settings.api_key = "YOUR_API_KEY"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(url)

print(transcript.text)