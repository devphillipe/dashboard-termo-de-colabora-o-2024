import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard de Economia", layout="wide")

# Função para formatação monetária
def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Criando o DataFrame com os dados
data = {
    "Mês": ["FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO", "OUTUBRO", "NOVEMBRO", "DEZEMBRO", "TOTAL"],
    "Valor Contrato": [2027087.81, 2050497.49, 2064930.37, 2055308.45, 2045686.53, 2026442.69, 2064930.37, 2060119.41, 2045686.53, 2055308.45, 2016175.65, 22512173.79],
    "Valor Pago": [2019387.81, 2044747.49, 2059480.37, 2050758.45, 2041186.53, 2021942.69, 2061130.37, 2056419.41, 2042036.53, 2051658.45, 2012375.65, 22461123.75],
    "Economia": [7700, 5750, 5450, 4550, 4500, 4500, 3800, 3700, 3650, 3650, 3800, 51050.04]
}

df = pd.DataFrame(data)

# Título principal
st.title("📊 Dashboard - Economia no Termo de Colaboração 2024")

# Layout de colunas para os primeiros dois gráficos
col1, col2 = st.columns(2)

# Gráfico 1: Valores do Contrato com Total
with col1:
    fig1 = px.bar(
        df, x="Mês", y="Valor Contrato",
        title="<b>VALORES DO CONTRATO</b>",
        labels={"Valor Contrato": "Valor (R$)", "Mês": "Mês"},
        text=df["Valor Contrato"].apply(format_currency)
    )
    fig1.update_traces(
        textposition="outside",
        textfont_size=12,
        marker_color='#1f77b4',
        marker_line_width=1.5
    )
    fig1.update_layout(
        title_x=0.5,
        title_font=dict(size=20),
        yaxis=dict(
            showticklabels=False,
            title_text=""
        )
    )
    st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Valores Pagos com Total
with col2:
    fig2 = px.bar(
        df, x="Mês", y="Valor Pago",
        title="<b>VALORES PAGOS</b>",
        labels={"Valor Pago": "Valor (R$)", "Mês": "Mês"},
        text=df["Valor Pago"].apply(format_currency)
    )
    fig2.update_traces(
        textposition="outside",
        textfont_size=12,
        marker_color='#ff7f0e',
        marker_line_width=1.5
    )
    fig2.update_layout(
        title_x=0.5,
        title_font=dict(size=20),
        yaxis=dict(
            showticklabels=False,
            title_text=""
        )
    )
    st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Comparação Total Contrato vs Pago
fig3 = px.bar(
    df[df["Mês"] == "TOTAL"].melt(value_vars=["Valor Contrato", "Valor Pago"]),
    x="variable", y="value", 
    title="<b>COMPARAÇÃO TOTAL: CONTRATO VS PAGO</b>",
    labels={"value": "Valor (R$)", "variable": ""},
    text=df[df["Mês"] == "TOTAL"].melt(value_vars=["Valor Contrato", "Valor Pago"])["value"].apply(format_currency)
)
fig3.update_traces(
    textposition="inside",
    textfont=dict(size=24, color="white"),
    marker_line_width=1.5,
    showlegend=False
)
fig3.update_layout(
    title_x=0.5,
    title_font=dict(size=20),
    xaxis=dict(title_text=""),
    yaxis=dict(showticklabels=False, showgrid=False, title_text="")
)
st.plotly_chart(fig3, use_container_width=True)

# Gráfico 4: Economia Mensal + Total
fig4 = px.bar(
    df, x="Mês", y="Economia",
    title="<b>ECONOMIA MENSAL E TOTAL</b>",
    labels={"Economia": "Valor Economizado (R$)", "Mês": "Mês"},
    text=df["Economia"].apply(format_currency)
)
fig4.update_traces(
    textposition="outside",
    textfont_size=12,
    marker_color='#2ca02c',
    marker_line_width=1.5
)
fig4.update_layout(
    title_x=0.5,
    title_font=dict(size=20),
    yaxis=dict(
        showticklabels=False,
        title_text=""
    )
)
st.plotly_chart(fig4, use_container_width=True)

# Tabela com formatação numérica correta
st.subheader("📋 TABELA DE DADOS COMPLETA")
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Mês": st.column_config.TextColumn("Mês"),
        "Valor Contrato": st.column_config.NumberColumn(
            "Valor Contrato (R$)",
            format="R$ %.2f"
        ),
        "Valor Pago": st.column_config.NumberColumn(
            "Valor Pago (R$)",
            format="R$ %.2f"
        ),
        "Economia": st.column_config.NumberColumn(
            "Economia (R$)",
            format="R$ %.2f"
        )
    }
)
