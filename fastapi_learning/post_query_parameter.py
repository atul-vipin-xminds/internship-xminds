from fastapi import FastAPI

app = FastAPI()

@app.post("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}
