import streamlit as st
import numpy as np
import pandas as pd
import requests

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

#esto va a leer del api
testo=st.text_input("Que",value="a")
url_base=f"http://modelo:80"
path=f"/predict/{testo}"
print(url_base+path)
respuesta=requests.get(url_base+path)

st.write(str(respuesta.content))
st.line_chart(chart_data)