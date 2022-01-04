from fastapi import FastAPI
import requests
import os
import xmltodict
import hashlib

API_URL = os.environ['API_URL']
API_SECRET_KEY = os.environ['API_SECRET_KEY']

checksum_hash = hashlib.sha1(f"getMeetings{API_SECRET_KEY}".encode())
checksum = checksum_hash.hexdigest()

app = FastAPI()

@app.get("/")
async def root():
    get_meetings_url = f'{API_URL}/getMeetings?checksum={checksum}'
    print(get_meetings_url)
    response = requests.get(get_meetings_url).content
    results = xmltodict.parse(response, force_list={'meeting'})
    return results