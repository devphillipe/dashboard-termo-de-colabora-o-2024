import streamlit as st
import pandas as pd
import plotly.express as px

# ⚠️ set_page_config precisa ser o primeiro comando Streamlit
st.set_page_config(page_title="Dashboard - Termo de Colaboração 2024", layout="wide")

# Criar DataFrame com os dados fornecidos
dados = {
    "MÊS": [
        "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO",
        "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO"
    ],
    "VALOR CONTRATO": [
        2027087.81, 2050497.49, 2064930.37, 2055308.45, 2045686.53, 
        2026442.69, 2064930.37, 2060119.41, 2045686.53, 2055308.45, 2016175.65
    ],
    "VALOR REAL PAGO": [
        2019387.81, 2044747.49, 2059480.37, 2050758.45, 2041186.53, 
        2021942.69, 2061130.37, 2056419.41, 2042036.53, 2051658.45, 2012375.65
    ],
    "DIF. CONTRATO x PAGO": [
        7700.00, 5750.00, 5450.00, 4550.00, 4500.00, 4500.00, 3800.00,
        3700.00, 3650.00, 3650.00, 3800.00
    ]
}

df = pd.DataFrame(dados)

# Criando o gráfico de economia mensal
fig = px.bar(
    df,
    x="MÊS",
    y="DIF. CONTRATO x PAGO",
    text="DIF. CONTRATO x PAGO",
    title="Economia Mensal - Termo de Colaboração 2024",
    labels={"DIF. CONTRATO x PAGO": "Diferença (R$)"},
    color="DIF. CONTRATO x PAGO",
    color_continuous_scale="greens"
)

# Ajustes no layout do gráfico
fig.update_traces(
    texttemplate="R$ %{y:,.2f}",
    textposition="outside"
)

fig.update_layout(
    xaxis_title="Mês",
    yaxis_title="Diferença em R$",
    margin=dict(l=50, r=50, t=50, b=80),
    coloraxis_showscale=False
)

# Exibir no Streamlit
st.title("📊 Termo de Colaboração 2024")
st.plotly_chart(fig, use_container_width=True)

# Mostrar a tabela com os dados
st.subheader("📋 Dados da Economia Mensal")
st.dataframe(df)
