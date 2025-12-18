# %%
import streamlit as st
import pandas as pd
import requests


# %%
URL = "https://viacep.com.br/ws/{cep}/json/"

st.title("buscar um cep")

cep = st.text_input("busque um cep")

if cep != "":
    resp = requests.get(URL.format(cep = cep))
    data = pd.DataFrame([resp.json()])
    st.dataframe(data)