import os

from functions import AudioTranscriber
import discord_notification
import settings

AUDIO_FILE = 'test.mp3'
audio_path = os.path.join(settings.AUDIO_DIR, AUDIO_FILE)
OUTPUT_FILE_NAME = AUDIO_FILE.split(".")[0]  # Do not need file extension


if __name__ == '__main__':
    transcriber = AudioTranscriber(model_name=settings.MODEL, lang=settings.LANG)
    minutes_dict = transcriber.audio_to_text(audio_path)
    transcriber.write_to_text("output.txt", minutes_dict)
    transcriber.export_csv("output.csv", minutes_dict)
    discord_notification.post_notice(message=f'{OUTPUT_FILE_NAME} minutes is DONE!')
