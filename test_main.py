import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TODO: make proper fixtures and teardowns 
# for request responses ``

def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}


def test_post_file_upload_csv(): 
    test_file = './test-data/generated_data/gen_data_v1.csv'
    files = {'file' : ('gen_data_v1.csv', open(test_file, 'rb'))}
    response = client.post('/file-upload', files=files)
    assert response.status_code == 200
    
def test_post_file_upload_excel(): 
    test_file = './test-data/generated_data/gen_data_v1.xlsx'
    files = {'file' : ('gen_data_v1.xlsx', open(test_file, 'rb'))}
    response = client.post('/file-upload', files=files)
    assert response.status_code == 200