# docker-fastapi

K8S demo 用的範例 app（所有章節共用的 image 來源）。

- `/`：回 `{"version": ...}`；**若 env 有 `DATABASE_HOST` / `LOG_LEVEL`（來自 ConfigMap/Secret）才會 echo 出來** → 沒 configmap 的章只看到 version，有 configmap 的章看得到設定。
- `/health`：`{"status":"ok"}`
- `version` 由 image 烤進去（`APP_VERSION` build-arg），所以 `:v1` 回 v1、`:v2` 回 v2。

## build & push

```bash
docker build --build-arg APP_VERSION=v1 -t yillkid/docker-fastapi:v1 .
docker build --build-arg APP_VERSION=v2 -t yillkid/docker-fastapi:v2 .
docker push yillkid/docker-fastapi:v1
docker push yillkid/docker-fastapi:v2
```

> 改了 image 後，minikube 若還快取舊的：`kubectl scale deploy <名> --replicas=0` → `minikube image rm yillkid/docker-fastapi:v1` → `minikube image load yillkid/docker-fastapi:v1` → scale 回來。
