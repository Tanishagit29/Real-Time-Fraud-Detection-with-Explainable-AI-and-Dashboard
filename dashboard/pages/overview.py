import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("processed_data.csv")

st.title("📊 Fraud Analytics Overview")

# Metrics
total_transactions = len(df)

critical = (
    df['RiskTier'] == 'Critical'
).sum()

suspicious = (
    df['RiskTier'] == 'Suspicious'
).sum()

avg_amt = df['TransactionAmt'].mean()

fraud_rate = (
    critical / total_transactions
) * 100

# KPI CARDS
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric(
        "Transactions",
        f"{total_transactions:,}"
    )

with col2:
    st.metric(
        "Critical Fraud",
        critical
    )

with col3:
    st.metric(
        "Fraud Rate %",
        round(fraud_rate,2)
    )

with col4:
    st.metric(
        "Avg Amount",
        f"${round(avg_amt,2)}"
    )

st.divider()

# Charts
col1,col2 = st.columns(2)

# Donut Chart
with col1:

    fig1 = px.pie(
        df,
        names='RiskTier',
        hole=0.6,
        title='Risk Tier Distribution'
    )

    fig1.update_layout(
        paper_bgcolor='#0E1117',
        plot_bgcolor='#0E1117',
        font_color='white'
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

# Hour Chart
with col2:

    hour_data = (
        df.groupby('HourOfDay')
        ['FraudProbability']
        .mean()
        .reset_index()
    )

    fig2 = px.line(
        hour_data,
        x='HourOfDay',
        y='FraudProbability',
        markers=True,
        title='Fraud Probability by Hour'
    )

    fig2.update_layout(
        paper_bgcolor='#0E1117',
        plot_bgcolor='#0E1117',
        font_color='white'
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# Histogram
fig3 = px.histogram(
    df,
    x='TransactionAmt',
    color='RiskTier',
    title='Transaction Amount Distribution',
    marginal='box'
)

fig3.update_layout(
    paper_bgcolor='#0E1117',
    plot_bgcolor='#0E1117',
    font_color='white'
)

st.plotly_chart(
    fig3,
    use_container_width=True
)