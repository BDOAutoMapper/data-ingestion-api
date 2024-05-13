import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TODO: make proper fixtures and teardowns 
# for request responses 

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    
def test_get_staged_files_success(): 
    response = client.get('/get-staged')
    assert response.status_code == 200
    assert response.json() == {"staged_files": [
        "temp_data\\temp_file.xlsx",
        "temp_data\\temp_file.txt"
    ]}

def test_post_file_upload_success(): 
    test_file = './temp_data/temp_file.xlsx'
    files = {'file' : ('test_file.xlsx', open(test_file, 'rb'))}
    response = client.post('/file-upload', files=files)
    assert response.status_code == 200
    assert response.json() == {"message": "File received successfully."}
    
def test_post_file_upload_bad_format(): 
    test_file = './temp_data/temp_file.txt'
    files = {'file' : ('test_file.txt', open(test_file, 'rb'))}
    response = client.post('/file-upload', files=files)
    assert response.status_code == 405
    assert response.json() == {"detail": "Uploaded file is not a valid Excel format."}