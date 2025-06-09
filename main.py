from fastapi import FastAPI
import json
from fastapi.responses import JSONResponse

app = FastAPI()


def load_data():
    try:
        with open("patients.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"error": "data.json not found"}
    except json.JSONDecodeError:
        return {"error": "Error decoding JSON from data.json"}

@app.get("/")

def hello():
    return {"message": "Hello, World!"}


@app.get("/about")

def about():
    return {"message": "This is a simple FastAPI application."}


@app.get("/view")

def view():
    data = load_data()
    if "error" in data:
        return JSONResponse(status_code=500, content=data)
    return data

@app.get("/health")
def health():
    return {"status": "healthy"}

