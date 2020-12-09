from fastapi import FastAPI
import requests
import json
import xmltodict
import imp

app = FastAPI()
def getVarFromFile(filename):
    f = open(filename)
    global data
    data = imp.load_source('data', filename, f)
    f.close()

@app.get("/")
async def root():
    getVarFromFile('/app/config.env')
    URL = (data.API_URL+'getMeetings')
    payload = 'checksum='+data.API_SECRET_KEY
    response = requests.get(URL, params=payload).content
    results = xmltodict.parse(response)
    return results