#esta es la api para comunicación con el modelo
from fastapi import FastAPI
from easy_model import modelo_complejo

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/{item_id}")
def read_item(item_id: str, q: int | None = None):
    return {"item_id": item_id, "q": q,"modelo_output":modelo_complejo()}