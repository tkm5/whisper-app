import os

from functions import AudioTranscriber
import discord_notification
import settings

AUDIO_FILE = 'audio.mp3'
audio_path = os.path.join(settings.AUDIO_DIR, AUDIO_FILE)
OUTPUT_FILE_NAME = AUDIO_FILE.split(".")[0]  # Do not need file extension


if __name__ == '__main__':
    transcriber = AudioTranscriber(model_name=settings.MODEL,
                                   lang=settings.LANG,
                                   use_api=True,
                                   )
    minutes_dict = transcriber.audio_to_text(audio_path)
    transcriber.write_to_text(f'{OUTPUT_FILE_NAME}.txt', minutes_dict)
    transcriber.export_csv(f'{OUTPUT_FILE_NAME}.csv', minutes_dict)
    discord_notification.post_notice(message=f'{OUTPUT_FILE_NAME} minutes is DONE!')
