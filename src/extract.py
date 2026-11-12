import os 
import camelot
import pandas as pd
import loguru
from unidecode import unidecode
from config import *

class PDFTableExtractor:
    def __init__(self, FILES_PATH, CONFIGS):
        self.path = os.path.abspath(f"{FILES_PATH}/{FILE_NAME}.pdf")
        self.csvpath = os.path.abspath(f"{CSV_PATH}/{FILE_NAME}.csv")
        self.configs = CONFIGS
        
    def start():
        pass

    def get_table_data(self, fix):
        tables = camelot.read_pdf(
            self.path,
            flavor=self.configs['flavor'],
            table_areas=self.configs['table_areas'],
            columns=self.configs['columns'],
            strip_text=self.configs['strip_text'],
            password=self.configs['password']
        )
        table_content = [self.fix_header(page.df)  if fix else page.df for page in tables]

    def add_infos():
        pass

    @staticmethod
    def fix_header(df):
        df.columns = df.columns.str.strip()
        df.columns = df.iloc[0]
        df = df.drop(0)
        df = df.drop(df.columns[0], axis=1)
        return df

    def sanitize_data():
        pass

if __name__ == "__main__":
    extractor = PDFTableExtractor()

    print(extractor)