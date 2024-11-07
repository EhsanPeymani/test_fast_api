# FAST API 

## uvicorn
Host the service using `uvicorn` to run service on ASGI server:
```
uvicorn src.main:app --host "0.0.0.0" --port 8000 --reload
```

## httpie
Invoke endpoints as
```
http localhost:8000
```