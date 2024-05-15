from fastapi import FastAPI, File, UploadFile, HTTPException
from pathlib import Path
import pandas as pd


VALID_APPLICATION_TYPES = [
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "text/csv",
]

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.post("/file-upload")
async def file_upload(file: UploadFile = File(...)):
    try:
        # TODO: Append filename instead of renaming to temp file
        if file.content_type != VALID_APPLICATION_TYPES[0]:
            transformed_data = transform_csv(file.file)
        else:
            transformed_data = transform_excel(file.file)
        response_data = transformed_data.to_json(orient="records")
        return {
            "message": "File processed successfully",
            "data": response_data,
            "application-type": file.content_type,
        }
    except Exception as e:
        raise HTTPException(status_code=405, detail={e})


def transform_excel(file):
    data = pd.read_excel(file)
    return data


def transform_csv(file):
    data = pd.read_csv(file, sep="delimiter")
    return data
