from fastapi import FastAPI

app = FastAPI()

@app.post("/student")
def create_student(student: dict):
    return {
        "name": student["name"],
        "course": student["course"]
    }