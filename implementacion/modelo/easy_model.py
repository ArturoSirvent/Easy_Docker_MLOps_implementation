from sklearn.linear_model import LinearRegression 
import scipy as sc
import numpy as np
import pandas as pd

def modelo_complejo(datos,h):
    X,y=datos
    #un modelo que nos devuelve la regresion lineal (prediccion) h steps en el futuro
    modelo=LinearRegression()
    modelo.fit(X,y)
    
    next_X=np.arange(np.max(X),np.max(X)+h)
    y_pred=modelo.predict(next_X)
    return y_pred