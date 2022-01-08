from fastapi import FastAPI
import requests
import os
import xmltodict
import hashlib
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets


API_URL = os.environ['API_URL']
API_SECRET_KEY = os.environ['API_SECRET_KEY']
USE_AUTH = os.environ['USE_AUTH']
AUTH_USERNAME = os.environ['AUTH_USERNAME']
AUTH_PASSWORD = os.environ['AUTH_PASSWORD']

checksum_hash = hashlib.sha1(f"getMeetings{API_SECRET_KEY}".encode())
checksum = checksum_hash.hexdigest()

app = FastAPI()
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, AUTH_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, AUTH_PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


if USE_AUTH in ['yes', 'Yes' , 'YES', True, 'true', 'TRUE']:
    password_require = Depends(get_current_username)
elif USE_AUTH in ['no', 'NO', 'No' , False , 'false' , 'FALSE']:
    password_require = None

@app.get("/")
async def root(username: str = password_require):
    get_meetings_url = f'{API_URL}/getMeetings?checksum={checksum}'
    response = requests.get(get_meetings_url).content
    results = xmltodict.parse(response, force_list={'meeting'})
    return results