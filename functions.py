import os

import whisper
import pandas as pd

import settings

LANG = settings.LANG

AUDIO_DIR = settings.AUDIO_DIR
AUDIO_FILE = settings.AUDIO_FILE
AUDIO_PATH = os.path.join(AUDIO_DIR, AUDIO_FILE)


def elapsed_time_str(seconds: float) -> str:
    """
    Convert seconds to a formatted time string (HH:MM:SS).

    Args:
        seconds (float): Time in seconds.

    Returns:
        str: Formatted time string in the format HH:MM:SS.
    """
    seconds = int(seconds + 0.5)
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60
    return f"{h:02}:{m:02}:{s:02}"


def audio_to_text(model: str) -> dict:
    """
    Convert audio files to text using the whisper model.

    Args:
        model (str): Path to the whisper model.

    Returns:
        dict: Dictionary containing the start time, end time, and text of each audio segment.
    """
    model = whisper.load_model(str(model))
    result_dict = model.transcribe(audio=AUDIO_PATH,
                                   verbose=True,
                                   language=LANG)
    minutes_dict = _generate_minutes_dict(result_dict['segments'])
    minutes_dict['start_time'] = [elapsed_time_str(t) for t in minutes_dict['start_time']]
    minutes_dict['end_time'] = [elapsed_time_str(t) for t in minutes_dict['end_time']]
    return minutes_dict


def _generate_minutes_dict(result: list) -> dict:
    """
    Generate dictionary of minutes from the transcribed result.

    Args:
        result (list): List of transcribed segments.

    Returns:
        dict: Dictionary containing the start time, end time, and text of each audio segment.
    """
    start_times_list = []
    end_times_list = []
    texts_list = []

    for segment in result:
        start_times_list.append(segment['start'])
        end_times_list.append(segment['end'])
        texts_list.append(segment['text'])

    return {
        'start_time': start_times_list,
        'end_time': end_times_list,
        'speach_text': texts_list
    }


def write_to_text(text_path: str, minutes_dict: dict):
    """
    Write transcribed minutes to a text file.

    Args:
        text_path (str): Path to the output text file.
        minutes_dict (dict): Dictionary containing the transcribed minutes.
    """
    with open(text_path, "w") as f:
        for i in range(len(minutes_dict["speach_text"])):
            print(f'[{minutes_dict["start_time"][i]}] --> [{minutes_dict["end_time"][i]}] | {minutes_dict["speach_text"][i]}',
                  file=f)


def export_csv(output_path: str, minutes_dict: dict):
    """
    Export transcribed minutes to a CSV file.

    Args:
        output_path (str): Path to the output CSV file.
        minutes_dict (dict): Dictionary containing the transcribed minutes.
    """
    df = pd.DataFrame(minutes_dict)
    df.to_csv(output_path)
