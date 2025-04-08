import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression, RANSACRegressor

# Upload do arquivo
arquivo = st.file_uploader("Envie seu arquivo Excel:", type=["xlsx"])

if arquivo:
    # Leitura e limpeza dos dados
    df = pd.read_excel(arquivo)
    df = df.rename(columns={'Tiny\nPESO SERRADO': 'Peso', 'preço novo': 'Preco'})
    df_limpo = df.dropna(subset=["Peso", "Preco"]).copy()

    # Modelo de regressão robusta
    modelo_base = LinearRegression()
    modelo_ransac = RANSACRegressor(estimator=modelo_base)
    x = df_limpo[["Peso"]]
    y = df_limpo[["Preco"]]
    modelo_ransac.fit(x, y)

    # Interface Streamlit
    st.title("Previsão do Valor do Pistão")

    # Entrada do usuário
    peso_input = st.number_input("Digite o peso do pistão (em kg):", min_value=0.0, format="%.3f")

    # Previsão
    if peso_input > 0:
        preco = modelo_ransac.predict([[peso_input]])[0][0]
        st.success(f"O preço estimado do pistão é: R$ {preco:.2f}")