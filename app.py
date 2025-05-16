import pandas as pd
import plotly.express as px
import streamlit as st
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt

dm = pd.read_csv('Tiempo_espera.csv')


st.title("Promedio de espera en el transmi")



Tab1, Tab2 = st.tabs(['Analisis Univariado', 'Analisis Bivariado'])

with Tab1:
    st.subheader("Distribución de variables numéricas")
    
    fig, ax = plt.subplots(2, 3, figsize=(10, 4))

    tab_freq = dm['Estacion'].value_counts().sort_index()
    ax[0, 0].bar(tab_freq.index, tab_freq.values)
    
    tab_freq = dm['Puntual'].value_counts().sort_index()
    ax[0, 1].bar(tab_freq.index, tab_freq.values)

    tab_freq = dm['Clima'].value_counts().sort_index()
    ax[0, 2].bar(tab_freq.index, tab_freq.values)

    tab_freq = dm['Demanda_alta'].value_counts().sort_index()
    ax[1, 0].bar(tab_freq.index, tab_freq.values)

    tab_freq = dm['Es_hora_pico'].value_counts().sort_index()
    ax[1,1].bar(tab_freq.index, tab_freq.values)

    fig.tight_layout()


    st.pyplot(fig)

    fig1 = px.histogram(dm, x='Hora', title ='Franja horaria')
    st.plotly_chart(fig1)

    fig2 = px.histogram(dm, x='Pasajeros',title= 'Pasajeros')
    st.plotly_chart(fig2)

    fig3 = px.histogram(dm, x='Tiempo_espera_min', title= 'Tiempo de espera minimo')
    st.plotly_chart(fig3)

with Tab2:
    st.subheader("Relación entre variables y el promedio de espera en el transmi")
    
    st.subheader("Hora Pico vs Tiempo de Espera")
    st.plotly_chart(px.box(dm, x='Es_hora_pico', y='Tiempo_espera_min'))

    st.subheader("Demanda Alta vs Tiempo de Espera")
    st.plotly_chart(px.box(dm, x='Demanda_alta', y='Tiempo_espera_min'))

    st.subheader("Puntualidad vs Tiempo de Espera")
    st.plotly_chart(px.box(dm, x='Puntual', y='Tiempo_espera_min'))
    
    fig4 = px.scatter(dm, x='Pasajeros', y='Tiempo_espera_min', title='')
    st.plotly_chart(fig4)

    fig5 = px.scatter(dm, x='Hora', y='Tiempo_espera_min', title='')
    st.plotly_chart(fig5)



