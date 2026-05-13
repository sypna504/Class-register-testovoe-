from pathlib import Path
import pandas as pd
from app.exceptions import InvalidFileFormatError
from fastapi import File

class CsvParser:
    def validate_extension(self, file):
        extension = Path(file.filename).suffix

        if extension!=".csv":
            raise InvalidFileFormatError("только .csv ")

    def read(self, file) -> pd.DataFrame:
        self.validate_extension(file)
        df = pd.read_csv(file.file)
        return df