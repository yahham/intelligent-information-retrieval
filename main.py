from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "message": "IIR - Intelligent Information Retrieval",
    }
