
import streamlit as st
import pickle
import numpy as np

# Título do app
st.title("💳 Detector de Fraudes em Transações")

# Carregar modelo
with open('modelo_fraude.pkl', 'rb') as f:
    modelo = pickle.load(f)

# Campos para entrada de dados (exemplo com 4 variáveis + amount)
v1 = st.number_input("V1", value=0.0)
v2 = st.number_input("V2", value=0.0)
v3 = st.number_input("V3", value=0.0)
v4 = st.number_input("V4", value=0.0)
amount = st.number_input("Valor da transação", value=50.0)

# Botão de previsão
if st.button("Verificar se é fraude"):
    entrada = np.array([[v1, v2, v3, v4, amount]])
    
    # Fazer a previsão
    predicao = modelo.predict(entrada)

    if predicao[0] == 1:
        st.error("🚨 Essa transação é FRAUDULENTA!")
    else:
        st.success("✅ Transação normal.")
