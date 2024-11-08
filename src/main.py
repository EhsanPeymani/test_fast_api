from fastapi import FastAPI, HTTPException
from mongita import MongitaClientDisk
from .data import get_people_data
from .models import Person


data_people = get_people_data()

app = FastAPI()

client = MongitaClientDisk()
db = client.db
people = db.people
people.insert_many(data_people)
print(people.count_documents({}))


@app.get("/")
async def root():
    return {"message", "Hello World"}


@app.get("/people")
async def get_people():
    existing_people = people.find({})
    existing_people_dict = {}
    existing_people_list_of_dict = []
    for person in existing_people:
        for key in person:
            if key == "_id":
                continue
            existing_people_dict[key] = person[key]
        existing_people_list_of_dict.append(existing_people_dict)
    return existing_people_list_of_dict


@app.get("/people/{person_id}")
async def get_person(person_id: int):
    if people.count_documents({"id": person_id}) > 0:
        person = people.find_one({"id": person_id})
        return {key: person[key] for key in person if key != "_id"}
    raise HTTPException(status_code=404, detail=f"No shape with id {person_id} found")


@app.post("/people")
async def post_person(person: Person):
    people.insert_one(person.model_dump())
    return person


@app.put("/peopel/{person_id}")
async def update_person(person_id: int, person: Person):
    if people.count_documents({"id": person_id}) > 0:
        people.replace_one({"id": person_id}, person.model_dump())
        return person
    raise HTTPException(status_code=404, detail=f"No person found with id {person_id}")


# upsert: update and insert if the document does not exist already
@app.put("/peopel/upsert/{person_id}")
async def update_person(person_id: int, person: Person):
    people.replace_one({"id": person_id}, person.model_dump(), upsert=True)
    return person


@app.delete(path="/people/{person_id}")
async def delete_person(person_id: int):
    deleted_person = people.delete_one({"id": person_id})
    if deleted_person.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"No person found with {person_id}")
    return {"OK": True}
