from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from GitHub Actions CI/CD! - created by hexxa"}