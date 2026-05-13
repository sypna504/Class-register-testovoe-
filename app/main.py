from fastapi import FastAPI, UploadFile, File
from app.db.connections import Connection
from app.routers.grades_router import router 

app = FastAPI(
    title="Grades API",
    version="1.0.0",
)

app.include_router(router)



