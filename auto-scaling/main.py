from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/load")
def load():
    time.sleep(0.5)  # Simulasi load
    return {"message": "load"}
