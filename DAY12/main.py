from fastapi import FastAPI, HTTPException, Request
import uvicorn
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

monuments = {
    "cobblestone": 45000,
    "granite": 25000,
    "marble": 20000,
    "limestone": 50000,
    "quartz": 30000
}


class MonumentsSchema(BaseModel):
    title: str = Field(max_length=30)
    price:  int = Field(gt=0)


@app.get("/monuments",
         summary='get_monuments',
         description='returns all monuments',
         tags=['monuments', 'get'])
def get_monuments(request: Request):
    if not monuments:
        raise HTTPException(status_code=404, detail='Not Found')
    return templates.TemplateResponse('index.html', {'request': request,
                                                     "monuments": monuments
                                                     }
                                      )


@app.post("/monuments/add/",
          summary='post_monuments',
          description='add new monument',
          tags=['monuments', 'post'])
def post_monuments(monument: MonumentsSchema):
    monuments[monument.title] = monument.price
    return {'message': 'ok'}


if __name__ == "__main__":
    uvicorn.run("main:app",
                port = 5003,
                reload=True)