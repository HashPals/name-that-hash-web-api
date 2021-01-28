from fastapi import FastAPI
import json
from mangum import Mangum
from name_that_hash import runner

app = FastAPI()


@app.get("/")
def read_root():
        return {"Hello": "World"}


@app.get("/api/{hash_string}")
def return_hash_id(hash_string: str):
    output = runner.api_return_hashes_as_json([hash_string])
    return json.loads(output)[hash_string]

handler = Mangum(app)
