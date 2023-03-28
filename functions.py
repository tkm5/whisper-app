import os

import whisper
import pandas as pd

import settings

LANG = settings.LANG

AUDIO_DIR = settings.AUDIO_DIR
AUDIO_FILE = settings.AUDIO_FILE
AUDIO_PATH = os.path.join(AUDIO_DIR, AUDIO_FILE)


def elapsed_time_str(seconds):
    seconds = int(seconds + 0.5)
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    return f"{h:02}:{m:02}:{s:02}"


def audio_to_text(model):
    # Convert audio files to text
    model = whisper.load_model(str(model))

    result_dict = model.transcribe(audio=AUDIO_PATH,
                                   verbose=True,
                                   language=LANG)

    minutes_dict = _generate_minutes_dict(result_dict['segments'])

    minutes_dict['start_time'] = [elapsed_time_str(t) for t in minutes_dict['start_time']]
    minutes_dict['end_time'] = [elapsed_time_str(t) for t in minutes_dict['end_time']]

    return minutes_dict


def _generate_minutes_dict(result):
    start_times_list = []
    end_times_list = []
    texts_list = []

    for result in result:
        start_time = result['start']
        start_times_list.append(start_time)
        end_time = result['end']
        end_times_list.append(end_time)
        text = result['text']
        texts_list.append(text)

    minutes_dict = {
        'start_time': start_times_list,
        'end_time': end_times_list,
        'speach_text': texts_list
    }

    return minutes_dict


def write_to_text(text_path, minutes_dict):
    with open(text_path, "w") as f:
        for i in range(len(minutes_dict)):
            print(f'[{minutes_dict["start_time"][i]}] --> [{minutes_dict["end_time"][i]}] | {minutes_dict["speach_text"][i]}',
                  file=f)


def export_csv(output_path, minutes_dict):
    df = pd.DataFrame(minutes_dict)
    df.to_csv(output_path)
