import streamlit as st
import pandas as pd
 
st.title(" Mini Análisis de Datos")
 
archivo = st.file_uploader("Sube un CSV", type="xlsx")
 
if archivo:
    df = pd.read_csv(archivo)
 
    st.subheader("Vista previa")
    st.dataframe(df.head())
 
    st.subheader("Estadísticas")
    st.write(df.describe())
 
    col = st.selectbox("Columna para graficar", df.select_dtypes("number").columns)
    st.bar_chart(df[col])
else:
    st.info("Sube un archivo CSV para empezar")