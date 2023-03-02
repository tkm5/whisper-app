import whisper
import pandas as pd

import slack_notification

LANG = "ja"
AUDIO_FILE = "test.m4a"
# Do not need file extension
OUTPUT_FILE_NAME = AUDIO_FILE.split(".")[0]


def elapsed_time_str(seconds):
    seconds = int(seconds + 0.5)
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - h * 3600 - m * 60

    return f"{h:02}:{m:02}:{s:02}"


def audio_to_text(model):
    # Convert audio files to text
    model = whisper.load_model(str(model))
    result_dict = model.transcribe(audio=AUDIO_FILE,
                                   verbose=True,
                                   language=LANG)
    return result_dict


def generate_start_time_end_time_text(result):

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

    return start_times_list, end_times_list, texts_list


def write_to_text(file_name=OUTPUT_FILE_NAME):
    with open(OUTPUT_FILE_NAME + ".txt", "w") as f:
        for i in range(len(texts)):
            print(f'[{start_times[i]}] --> [{end_times[i]}] | {texts[i]}', file=f)


def export_csv(output_file_name=OUTPUT_FILE_NAME):
    df = pd.DataFrame(data={'start_time': start_times,
                            'end_time': end_times,
                            'speach_text': texts}
                      )
    df.to_csv(OUTPUT_FILE_NAME + ".csv")


results = audio_to_text(model="large")
start_times, end_times, texts = generate_start_time_end_time_text(results['segments'])

start_times = list(map(elapsed_time_str, start_times))
end_times = list(map(elapsed_time_str, end_times))

write_to_text()
export_csv()
slack_notification.slack_dm()
