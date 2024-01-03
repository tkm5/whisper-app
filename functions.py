import os
import whisper
import pandas as pd

import settings


class AudioTranscriber:
    """A class for transcribing audio files to text.

    Attributes:
        model (whisper.Model): An instance of the Whisper model.
        lang (str): Language to use for transcription.
    """

    def __init__(self, model_name: str, lang: str):
        """Initializes the AudioTranscriber class with a specific Whisper model and language.

        Args:
            model_name (str): Name of the Whisper model to be used.
            lang (str): Language to be used for transcription.
        """
        self.model = whisper.load_model(model_name)
        self.lang = lang

    @staticmethod
    def elapsed_time_str(seconds: float) -> str:
        """Converts elapsed time in seconds to a formatted string (hh:mm:ss).

        Args:
            seconds (float): Elapsed time in seconds.

        Returns:
            str: Formatted time string in hh:mm:ss format.
        """
        seconds = int(seconds + 0.5)
        h = seconds // 3600
        m = (seconds - h * 3600) // 60
        s = seconds - h * 3600 - m * 60
        return f"{h:02}:{m:02}:{s:02}"

    @staticmethod
    def _generate_minutes_dict(result: list) -> dict:
        """Generates a dictionary with start times, end times, and transcribed text from the results.

        Args:
            result (list): List of transcription results.

        Returns:
            dict: Dictionary containing start times, end times, and speech text.
        """
        return {
            'start_time': [segment['start'] for segment in result],
            'end_time': [segment['end'] for segment in result],
            'speach_text': [segment['text'] for segment in result]
        }

    @staticmethod
    def write_to_text(text_path: str, minutes_dict: dict):
        """Writes the transcription results to a text file.

        Args:
            text_path (str): Path to the output text file.
            minutes_dict (dict): Dictionary of transcription results per minute.
        """
        with open(text_path, "w") as f:
            for i in range(len(minutes_dict["speach_text"])):
                print(
                    f'[{minutes_dict["start_time"][i]}] --> [{minutes_dict["end_time"][i]}] | {minutes_dict["speach_text"][i]}',
                    file=f)

    @staticmethod
    def export_csv(output_path: str, minutes_dict: dict):
        """Exports the transcription results to a CSV file.

        Args:
            output_path (str): Path to the output CSV file.
            minutes_dict (dict): Dictionary of transcription results per minute.
        """
        df = pd.DataFrame(minutes_dict)
        df.to_csv(output_path)

    def audio_to_text(self, audio_path: str) -> dict:
        """Transcribes an audio file to text.

        Args:
            audio_path (str): Path to the audio file to be transcribed.

        Returns:
            dict: Dictionary containing the transcription results.
        """
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        result_dict = self.model.transcribe(audio=audio, verbose=True, language=self.lang)
        minutes_dict = self._generate_minutes_dict(result_dict['segments'])
        minutes_dict['start_time'] = [self.elapsed_time_str(t) for t in minutes_dict['start_time']]
        minutes_dict['end_time'] = [self.elapsed_time_str(t) for t in minutes_dict['end_time']]
        return minutes_dict
