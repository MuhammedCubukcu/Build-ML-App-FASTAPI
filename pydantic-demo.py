from pydantic import BaseModel


data = {
    "name": "Muhammed",
    "age": 25,
    "course": "MlOps BootCamp",
    "ratings": [4,4,"4","5",4]
}

class Instructor(BaseModel):
    name: str
    age: int
    course: str
    ratings: list[int] = []

user = Instructor(**data)
print(f"Found a Instructor {user}")