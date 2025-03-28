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

# Gráfico 1: Comparação Valor Contrato vs Valor Pago por mês
df_melted = df[df["Mês"] != "TOTAL"].melt(id_vars=["Mês"], value_vars=["Valor Contrato", "Valor Pago"], var_name="Tipo", value_name="Valor")

fig1 = px.bar(
    df_melted, x="Mês", y="Valor", color="Tipo",
    title="<b>Comparação Mensal: Valor do Contrato vs Valor Pago</b>",
    labels={"Valor": "Valor (R$)", "Mês": "Mês"},
    barmode="group",
    text=df_melted["Valor"].apply(lambda x: f'R$ {x/1e6:.2f}M')
)

fig1.update_traces(
    textposition="outside",
    textfont_size=14,
    marker_line_width=1.5
)

fig1.update_layout(
    yaxis=dict(
        range=[1900000, 2150000],
        tickprefix="R$ ",
        ticksuffix=" ",
        tickformat=".2s",
        title_font=dict(size=14)
        )
)
st.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Comparação Total do Contrato vs Total Pago (valores centralizados)
df_total = df[df["Mês"] == "TOTAL"].melt(value_vars=["Valor Contrato", "Valor Pago"], var_name="Tipo", value_name="Valor")

fig2 = px.bar(
    df_total, x="Tipo", y="Valor", color="Tipo",
    title="<b>Total do Contrato vs Total Pago</b>",
    labels={"Valor": "Valor (R$)", "Tipo": ""},
    text=df_total["Valor"].apply(lambda x: f'R$ {x/1e6:.2f}M')
)

fig2.update_traces(
    textposition="inside",
    textfont=dict(size=24, color="white"),
    marker_line_width=1.5,
    showlegend=False
)

fig2.update_layout(
    xaxis=dict(title_text=""),
    yaxis=dict(showticklabels=False, showgrid=False, title_text="")
)

st.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Economia Mensal + Economia Total
fig3 = px.bar(
    df, x="Mês", y="Economia",
    title="<b>Economia Mensal e Total</b>",
    labels={"Economia": "Valor Economizado (R$)", "Mês": "Mês"},
    text=df["Economia"].apply(lambda x: f'R$ {x/1e3:.1f}K'),
    color="Economia",
    color_continuous_scale="Blues"
)

fig3.update_traces(
    textposition="outside",
    textfont_size=12,
    marker_line_width=1.5
)

st.plotly_chart(fig3, use_container_width=True)

# Tabela com dados formatados
st.subheader("📋 Tabela de Dados")
df_display = df.copy()
for col in ["Valor Contrato", "Valor Pago", "Economia"]:
    df_display[col] = df[col].apply(format_currency)
    
st.dataframe(
    df_display,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Mês": "Mês",
        "Valor Contrato": st.column_config.NumberColumn("Valor Contrato", format="R$ %.2f"),
        "Valor Pago": st.column_config.NumberColumn("Valor Pago", format="R$ %.2f"),
        "Economia": st.column_config.NumberColumn("Economia", format="R$ %.2f")
    }
)
