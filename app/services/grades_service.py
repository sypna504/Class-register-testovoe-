from app.parsers.csv_parser import CsvParser
from app.validators.grades_validator import Validator
from app.repositories.grades_repository import GradesRepository
import pandas as pd



class GradeServices:
    def __init__(self):
        self.parser = CsvParser()
        self.validator = Validator()
        self.repository = GradesRepository()
    
    def grades_from_csv(self, file):
        df = self.parser.read(file)
        self.validator.validate(df)
        rows = []
        for _, row in df.iterrows():
            rows.append((row["student"], row["grade"]))
        self.repository.insert_into_table(rows)
        return {
            "status": "ok",
            "records_loaded": len(df),
            "students": df["student"].nunique()
        }
        

    def get_students_with_twos(self, more_than=None, les_than=None):
        rows = self.repository.get_students_by_twos_count(more_than=more_than, les_than=les_than,)
        students = []
        for student, count_twos in rows:
            students.append({
                "full_name": student,
                "count_twos": count_twos,
            })

        return {
            "students": students
        }

    

    
        

    