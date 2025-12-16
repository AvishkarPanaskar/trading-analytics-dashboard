import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("Live Trading Analytics")

conn = sqlite3.connect("ticks.db")
df = pd.read_sql("SELECT * FROM ticks", conn)

if df.empty:
    st.warning("Waiting for data...")
else:
    symbols = st.multiselect(
        "Select Symbols",
        df.symbol.unique(),
        default=df.symbol.unique()[:2]
    )

    df = df[df.symbol.isin(symbols)]

    fig = px.line(df, x="ts", y="price", color="symbol")
    st.plotly_chart(fig, use_container_width=True)

    df["z"] = (df.price - df.price.mean()) / df.price.std()
    st.line_chart(df["z"])

    threshold = st.slider("Z-Score Alert", 1.0, 3.0, 2.0)
    if abs(df["z"].iloc[-1]) > threshold:
        st.error("🚨 Z-Score Alert Triggered")

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "analytics.csv"
    )
