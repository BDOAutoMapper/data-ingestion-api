import shutil, io
from fastapi import FastAPI, File, UploadFile, HTTPException
import openpyxl
from pathlib import Path
from typing import Callable


class Input:
    name: str
    type: str


FILE_PATH = "./temp_data/temp_file.xlsx"
FOLDER_PATH = Path("./temp_data/")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/get-staged")
async def get_staged_files():
    contents_iter = FOLDER_PATH.iterdir()
    contents = [c.name for c in contents_iter]
    # contents = [*contents_iter]
    return {"staged_files": contents}

    assert file is not None
    assert file.filename.endswith(".xlsx")
    try:
        # TODO: Append filename instead of renaming to temp file
        with open(FILE_PATH, "wb") as f:
            f.write(file.file.read())
    except Exception as E:
        raise HTTPException(
            status_code=405, detail="Uploaded file is not a valid Excel format."
        )
    finally:
        f.close()
        return {"message": "File received successfully."}


@app.post("/file-upload")
async def file_upload(file: UploadFile):
    assert file is not None
    if file.filename.endswith(".xlsx") == False:
        raise HTTPException(
            status_code=405, detail="Uploaded file is not a valid Excel format."
        )
    try:
        # TODO: Append filename instead of renaming to temp file
        with open(FILE_PATH, "wb") as f:
            f.write(file.file.read())
    except Exception as E:
        raise HTTPException(
            status_code=405, detail="Uploaded file is not a valid Excel format."
        )
    finally:
        f.close()
        return {"message": "File received successfully."}
