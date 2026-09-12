import streamlit as st
import numpy as np
import libreria_funciones as lf

st.title("Especializacion python for analytics")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Anibal Minaya")

st.image("Python_logo.png",width =300)

st.sidebar.image("DMC.png")

modulos = st.sidebar.selectbox("Seleccione el módulo",["Listas","Arreglos","Funciones","POO" ])

if modulos == "Listas":
  st.write("Te encuentras en el módulo de listas")
  valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango",value=0))
  valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))
  Lista = list(range(valor_inicial,valor_final))
  st.write(Lista)
  
elif modulos == "Arreglos":
  st.write("Te encuentras en el módulo de arreglos")

  cantidad=st.slider("Seleccione un valor del rango",min_value=1,max_value=100,value=20)
  arreglo = np.arange(cantidad)

  st.write(arreglo)

elif modulos == "Funciones":
  
  st.write("Te encuentras en el módulo de funciones")
  
  capital_i = st.number_input("Ingrese el capital inicial", min_value=0 ,max_value = 10000, value = 1000)
  aporte_m = st.number_input("Ingrese el aporte mensual",min_value=0,max_value=10000,value=100)
  tasa_a = st.slider("Ingrese la tasa",min_value=0.01,max_value=1.00,value=0.05)
  anios = st.slider("Ingrese la tasa",min_value=1,max_value=20,value=2)

  resultado_valor_futuro=lf.valor_futuro_inversion(capital_i,aporte_m,tasa_a,anios)
  st.write("El resultado de tu valor futuro de inversion es: ",resultado_valor_futuro)
else:
  st.write("Te encuentras en el módulo de POO")
