# FAST API 
This is a small project to practice FastAPI and Mongita.


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

## Usage

Use the open.documentation at

```
http://0.0.0.0:8000/docs
```