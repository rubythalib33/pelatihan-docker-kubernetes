from fastapi import FastAPI
import os

app = FastAPI()

def log_to_server():
    os.makedirs('data', exist_ok=True)
    with open('data/data.txt','a') as f:
        f.write('HALO\n')
        f.close()

@app.get('/')
def hello_world():
    log_to_server()
    return {"message": "hello world"}


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host=os.getenv('HOST', '127.0.0.1'))