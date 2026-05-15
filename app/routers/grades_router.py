from fastapi import APIRouter, UploadFile, File, HTTPException
from app.grades_service import GradesService
from app.schemas.grades_schema import FileUploadedResponse, StudentTwosCount
from app.grades_service import Validator
from app.parsers.csv_parser import CsvParser
from app.db.grades_repository import GradesRepository
from app.exceptions import AppError
"""файл с http-эндпоинтами для работы с оценками студентов
здесь описаны маршруты для загрузки csv файла и получения студентов
по количеству 2"""

"""роутер для эндпоинтов"""
router = APIRouter()

@router.post(path="/upload-grades",
            response_model=FileUploadedResponse)

async def upload_grades(file:UploadFile = File(...)):
    """принимает csv файл проверяет его и сохраняет в базу"""
    
    try:
        parser = CsvParser()
        validator = Validator()
        repository = GradesRepository()
        return GradesService(
            parser=parser, 
            validator=validator,
            repository=repository).grades_from_csv(file)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
    
    except Exception as ex:
        raise HTTPException(status_code=422, detail=str(ex))
    
        

@router.get(path="/students/more-than-3-twos",
            response_model=list[StudentTwosCount])
async def get_more_than_3_twos():
    """возвращает студентов у которых болше трех 2"""

    try:
        parser = CsvParser()
        validator = Validator()
        repository = GradesRepository()
        return GradesService(
            parser=parser, 
            validator=validator,
            repository=repository).get_students_with_twos(more_than=3)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
    
    except Exception as ex:
        raise HTTPException(status_code=422, detail=str(ex))
    


@router.get(path="/students/less-than-5-twos",
            response_model=list[StudentTwosCount])
async def get_less_than_5_twos():
    """возвращает студентов у которых меньше пяти 2"""

    try:
        parser = CsvParser()
        validator = Validator()
        repository = GradesRepository()
        return GradesService(
            parser=parser, 
            validator=validator,
            repository=repository).get_students_with_twos(les_than=5)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
    
    except Exception as ex:
        raise HTTPException(status_code=422, detail=str(ex))
