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
def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

df_display = df.copy()
df_display["Valor Contrato"] = df["Valor Contrato"].apply(format_currency)
df_display["Valor Pago"] = df["Valor Pago"].apply(format_currency)
df_display["Economia"] = df["Economia"].apply(format_currency)

# Título principal
st.title("📊 Dashboard - Economia no Termo de Colaboração 2024")

# Gráfico 1: Comparação Valor Contrato vs Valor Pago por mês (Gráfico de Linhas com ajuste de escala)
fig1 = px.line(
    df, x="Mês", y=["Valor Contrato", "Valor Pago"],
    title="Comparação Mensal: Valor do Contrato vs Valor Pago",
    labels={"value": "Valor (R$)", "Mês": "Mês", "variable": "Tipo"},
    markers=True
)

# Ajustando a escala para valores mensais
fig1.update_layout(
    yaxis_tickformat=",.0f",  # Exibindo os valores sem casas decimais
    yaxis=dict(tickprefix="R$ ", range=[0, 3000000])  # Ajustando a escala para 3 milhões
)

# Adicionar os valores nos pontos
for trace in fig1.data:
    trace.update(text=[format_currency(v) for v in trace.y], textposition="top center", textfont_size=14, mode="markers+text")

# Gráfico 2: Comparação Total do Contrato vs Total Pago (Valores no Centro)
df_total = df[df["Mês"] == "TOTAL"].melt(id_vars=["Mês"], value_vars=["Valor Contrato", "Valor Pago"], var_name="Tipo", value_name="Valor")

fig2 = px.bar(
    df_total, x="Tipo", y="Valor", color="Tipo",
    title="Total do Contrato vs Total Pago",
    labels={"Valor": "Valor (R$)", "Tipo": "Tipo"},
    text=df_total["Valor"].apply(format_currency)  # Exibir os valores formatados
)

fig2.update_traces(textposition="inside", textfont_size=16)  # Valores no centro das barras

st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Economia Mensal + Economia Total (Barras com valores visíveis)
fig3 = px.bar(
    df, x="Mês", y="Economia",
    title="Economia Mensal e Total",
    labels={"Economia": "Valor Economizado (R$)", "Mês": "Mês"},
    text=df["Economia"].apply(format_currency),  # Exibir os valores formatados
    color="Economia"
)

fig3.update_traces(textposition="outside", textfont_size=14)  # Valores acima das barras, com fonte maior

st.plotly_chart(fig3, use_container_width=True)

# Exibir a tabela com os dados formatados
st.subheader("📋 Tabela de Dados")
st.dataframe(df_display, use_container_width=True)
