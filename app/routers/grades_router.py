from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.grades_service import GradeServices
from app.schemas.grades_schema import FileSuccesfullUploaded, StudentsTwosResponse
from app.exceptions import (
    InvalidFileFormatError,
    IncorrectFileColumnsError,
    IncorrectStudentColumnError,
    IncorrectGradeRangeError,
    EmptyCsvFileError,
    AppError,
)

router = APIRouter()

@router.post(path="/upload-grades",
            response_model=FileSuccesfullUploaded)

async def upload_grades(file:UploadFile = File(...)):
    try:
        return GradeServices().grades_from_csv(file)
    except InvalidFileFormatError as ex:
        raise HTTPException(status_code=400, detail=ex.message)
    
    except EmptyCsvFileError as ex:
        raise HTTPException(status_code=400, detail=ex.message)
    except IncorrectFileColumnsError as ex:
        raise HTTPException(status_code=422, detail=ex.message)

    except IncorrectStudentColumnError as ex:
        raise HTTPException(status_code=500, detail=ex.message)

    except IncorrectGradeRangeError as ex:
        raise HTTPException(status_code=500, detail=ex.message)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
        

@router.get(path="/students/more-than-3-twos",
            response_model=StudentsTwosResponse)
async def get_more_than_3_twos():
    try:
        return GradeServices().get_students_with_twos(more_than=3)
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex.message)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
    


@router.get(path="/students/less-than-5-twos",
            response_model=StudentsTwosResponse)
async def get_less_than_5_twos():
    try:
        return GradeServices().get_students_with_twos(les_than=5)
    
    except Exception as ex:
        raise HTTPException(status_code=500, detail=ex.message)
    
    except AppError as ex:
        raise HTTPException(
            status_code=422,
            detail={
                "message": ex.message,
                "field": ex.field_name,
                "code": ex.error_code,
            },
        )
