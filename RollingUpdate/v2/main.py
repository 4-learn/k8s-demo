from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"version": "v2", "fix": "resolved timeout issue"}
