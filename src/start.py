import os 
import camelot
import pandas as pd
import loguru
from unidecode import unidecode
from config import *

class PDFTableExtractor:
    def __init__(self, FILES_PATH,CONFIGS):
        self.path = os.path.abspath(f"{FILES_PATH}/{FILE_NAME}.pdf")

    def start():
        pass

    def get_table_data():
        pass

    def save_csv():
        pass

    def add_info():
        pass

    def fix_head():
        pass

    def sanitize_data():
        pass

    def send_to_db():
        pass

if __name__ == "__main__":
    extractor = PDFTableExtractor()

    print(extractor)