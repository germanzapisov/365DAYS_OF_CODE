from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

class Monument(BaseModel):
    title: str
    price: int

app = FastAPI()

monuments = {
        "granit": 15000,
        "mramore": 35000
     }


@app.get("/monuments")
def func_monument():
    return monuments

@app.post("/monuments")
def add_monument(monument: Monument):
    monuments[monument.title] = monument.price
    return {"message": f"Монумент '{monument.title}' добавлен", "monuments": monuments}


if __name__ == "__main__":
    uvicorn.run("main:app", port = 5000, reload=True)

