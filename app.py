import streamlit as st

st.title("Especializacion python for analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Anibal Minaya")

modulos = st.sidebar.selectbox("Seleccione el módulo",["Listas","Arreglos","Funciones","POO" ])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")
  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango",value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))
  Lista = list(range(valor_inicial,valor_final))
  st.write(Lista)
  
elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")
elif modulos == "Funciones":
  st.write("Te encuentras en el módulo de funciones")
else:
  st.write("Te encuentras en el módulo de POO")
