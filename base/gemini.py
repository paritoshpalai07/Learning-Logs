from google import genai
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.getenv("SECRET_KEY")

def get_video_id(str):
    list = str.split("https://youtu.be/")
    video_id = list[1].split("?si=")[0]
    return video_id

def notes(vidurl):
    vid_id = get_video_id(vidurl)
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(vid_id, languages=['en','hi'])
    transcript = ''.join([snippet.text+' ' for snippet in fetched_transcript])
    prompt = f'make summary and notes of the given transcript of a youtube video. provide only summary and notes not anything else. the transcript: {transcript}'



    client = genai.Client(api_key=secret_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )

    note = response.text.replace("transcript", "")
   
    return [note, transcript]
