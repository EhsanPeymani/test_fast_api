from fastapi import FastAPI, HTTPException


app = FastAPI()

PEOPLE = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "age": 28, "gender": "male"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "age": 34, "gender": "female"},
    {"id": 3, "first_name": "Alice", "last_name": "Johnson", "age": 22, "gender": "female"},
    {"id": 4, "first_name": "Bob", "last_name": "Brown", "age": 45, "gender": "male"}
]


@app.get("/")
async def root():
    return {"message", "Hello World"}


@app.get("/people")
async def get_people():
    return PEOPLE


@app.get("/people/{person_id}")
async def get_person(person_id: int):
    for p in PEOPLE:
        if p["id"] == person_id:
            return p
        
    raise HTTPException(status_code=404, detail=f"No shape with id {person_id} found")