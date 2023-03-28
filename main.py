import os

import functions
import settings

OUTPUT_FILE_NAME = settings.OUTPUT_FILE_NAME

TEXT_DIR = settings.TEXT_DIR
CSV_DIR = settings.CSV_DIR

TEXT_PATH = os.path.join(TEXT_DIR, OUTPUT_FILE_NAME+".txt")
CSV_PATH = os.path.join(CSV_DIR, OUTPUT_FILE_NAME+".csv")

if __name__ == '__main__':
    minutes_dict = functions.audio_to_text(model='large')
    functions.write_to_text(TEXT_PATH, minutes_dict)
    functions.export_csv(CSV_PATH, minutes_dict)
