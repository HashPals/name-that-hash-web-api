from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from mangum import Mangum
from name_that_hash import runner
import base64

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/{hash_string}")
def return_hash_id(hash_string: str):
    headers = {
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Origin": "https://nth.skerritt.blog",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
    }
    hash_string = base64.b64decoode(hash_string)
    output = json.loads(runner.api_return_hashes_as_json([hash_string]))
    return JSONResponse(content=output[hash_string], headers=headers)


handler = Mangum(app)
