from pathlib import Path
import pandas as pd
from app.exceptions import InvalidFileFormatError

class CsvParser:
    """парсер для файлов типа .csv"""

    def validate_extension(self, file) -> None:
        """функция для првоерки типа файла"""

        extension = Path(file.filename).suffix

        if extension!=".csv":
            raise InvalidFileFormatError("только .csv ")

    def read(self, file) -> pd.DataFrame:
        """функция для чтения файла """
        
        self.validate_extension(file)
        df = pd.read_csv(file.file)
        return df