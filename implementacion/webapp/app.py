import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import ast

#esto va a leer del api
valor=st.text_input("¿Cuántos más predecir?",value=12)
url_base=f"http://modelo:80"
path=f"/predict/{valor}"
print(url_base+path)
respuesta=requests.get(url_base+path)

st.write(str(respuesta.content))

#sacamos la info de la respuesta
resp_dict=ast.literal_eval(str(respuesta.content))

st.line_chart( np.concatenate((resp_dict["datos"][0],resp_dict["prediccion"])))