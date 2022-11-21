#esta es la api para comunicación con el modelo
from fastapi import FastAPI
from easy_model import modelo_complejo
import numpy as np


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#datos=#como si nos los estuvieran pasando los IoTs
a=3
b=10
x=np.random.uniform(0,10,100)
x.sort()
datos=(x,list(np.random.randn(100)+x*a+b))

@app.get("/predict/{valor}")
def read_item(valor: int = 5):
    return {"datos": datos, "h": valor,}#"prediccion":modelo_complejo(datos=datos,h=valor)}