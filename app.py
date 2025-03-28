import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Economia", layout="wide")

# Criando o DataFrame com os dados
data = {
    "Mês": ["FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO", "TOTAL"],
    "Valor Contrato": [2027087.81, 2050497.49, 2064930.37, 2055308.45, 2045686.53, 2026442.69, 2064930.37, 2060119.41, 2045686.53, 2055308.45, 2016175.65, 22512173.79],
    "Valor Pago": [2019387.81, 2044747.49, 2059480.37, 2050758.45, 2041186.53, 2021942.69, 2061130.37, 2056419.41, 2042036.53, 2051658.45, 2012375.65, 22461123.75],
    "Economia": [7700, 5750, 5450, 4550, 4500, 4500, 3800, 3700, 3650, 3650, 3800, 51050.04]
}

df = pd.DataFrame(data)

# Criar colunas formatadas para exibição
df_display = df.copy()
df_display["Valor Contrato"] = df["Valor Contrato"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_display["Valor Pago"] = df["Valor Pago"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
df_display["Economia"] = df["Economia"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Título principal
st.title("📊 Dashboard - Economia no Termo de Colaboração 2024")

# Gráfico 1: Comparação Valor Contrato vs Valor Pago por mês
fig1 = px.bar(
    df, x="Mês", y=["Valor Contrato", "Valor Pago"],
    title="Comparação Mensal: Valor do Contrato vs Valor Pago",
    labels={"value": "Valor (R$)", "Mês": "Mês"},
    barmode="group",
    text_auto=True
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Comparação Total do Contrato vs Total Pago
df_total = df[df["Mês"] == "TOTAL"].melt(id_vars=["Mês"], value_vars=["Valor Contrato", "Valor Pago"])

fig2 = px.bar(
    df_total, x="Mês", y="value", color="variable",
    title="Total do Contrato vs Total Pago",
    labels={"value": "Valor (R$)", "Mês": "Total"},
    text_auto=True
)
st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Economia Mensal + Economia Total
fig3 = px.bar(
    df, x="Mês", y="Economia",
    title="Economia Mensal e Total",
    labels={"Economia": "Valor Economizado (R$)", "Mês": "Mês"},
    text_auto=True,
    color="Economia"
)
st.plotly_chart(fig3, use_container_width=True)

# Exibir a tabela com os dados formatados
st.subheader("📋 Tabela de Dados")
st.dataframe(df_display, use_container_width=True)
