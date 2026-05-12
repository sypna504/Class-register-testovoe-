from fastapi import FastAPI, UploadFile, File, HTTPException
from pathlib import Path
import pandas as pd
from app.db.conections import Connection

app = FastAPI()

@app.post("/upload-grades")
async def upload_grades(file:UploadFile = File(...)):
    extention = Path(file.filename).suffix

    if extention!=".csv":
        raise HTTPException(status_code=409, detail="wrong file formate")
    
    df = pd.read_csv(file.file)
    if "student" not in df.columns or "grade" not in df.columns:
        raise HTTPException(status_code=409, detail="no such columns in dataframe")
    
    df = df.dropna()
    df["student"] = df["student"].astype("str")
    df["grade"] = df["grade"].astype("int")
    if (((df["grade"]<0) | (df["grade"]>5))).any():
        raise HTTPException(status_code=409, detail="grade is not in correct range")
    
    rows = []
    for _, row in df.iterrows():
        rows.append((row["student"], row["grade"]))
    try:
        conn = Connection().get_conn()
        cur = conn.cursor()
        cur.execute("TRUNCATE TABLE grades")
        for row in rows:
            try:
                cur.execute(
                    "INSERT INTO grades (student, grade) VALUES (%s, %s)",
                    row,
                )
            except Exception as ex:
                raise HTTPException(status_code=409, detail=str(ex)) 
        conn.commit()
        cur.close()
    except Exception as ex:
        raise HTTPException(status_code=409, detail=str(ex))


    students_count = df["student"].nunique()
    loads = len(df)
    return {"status": "ok",
            "records_loaded": loads,
            "students": students_count
            }

@app.get("/students/more-than-3-twos")
async def get_more_than_3_twos():
    try:
        res=[]
        conn = Connection().get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT student, COUNT(*) AS grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)>3"
        )
        rows = cur.fetchall()
        for student,cnt in rows:
            res.append({
                "full_name": student,
                "count_twos": cnt,
            })
        cur.close()
        conn.close()
        return {
            "students": res,
            }
    except Exception as ex:
        raise HTTPException(status_code=409, detail=str(ex))


@app.get("/students/less-than-5-twos")
async def get_less_than_5_twos():
    try:
        res = []
        conn = Connection().get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT student, COUNT(*) as grade_cnt FROM grades WHERE grade=2 GROUP BY student HAVING COUNT(*)<5"
        )
        rows = cur.fetchall()
        for student,cnt in rows:
            res.append({
                "full_name": student,
                "count_twos": cnt,
            })

        cur.close()
        conn.close()
        return {
            "students": res,
        }
    except Exception as ex:
        raise HTTPException(status_code=409, detail=str(ex))


