from fastapi import FastAPI
from app.models.inference import predict

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "ok"}


@app.post("/predict")
def predict_route(input: dict):
    return {"prediction": predict(input)}
