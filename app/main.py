from fastapi import FastAPI
from app.routers.grades_router import router 

"""наше приложение"""
app = FastAPI()

"""роутер"""
app.include_router(router)



