import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    # 只有 env 真的有設定（來自 ConfigMap/Secret）才 echo，沒有就只回 version
    resp = {}
    if os.environ.get("DATABASE_HOST"):
        resp["db_host"] = os.environ["DATABASE_HOST"]
    if os.environ.get("LOG_LEVEL"):
        resp["log_level"] = os.environ["LOG_LEVEL"]
    resp["version"] = os.environ.get("APP_VERSION", "v1")   # version 由 image 烤進去
    return resp


@app.get("/health")
def health():
    return {"status": "ok"}
