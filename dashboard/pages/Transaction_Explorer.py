import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("processed_data.csv")

st.title("🔍 Transaction Explorer")

# Sidebar
st.sidebar.header("Filters")

risk = st.sidebar.multiselect(
    "Risk Tier",
    df['RiskTier'].unique(),
    default=df['RiskTier'].unique()
)

filtered_df = df[
    df['RiskTier'].isin(risk)
]

# Search
search = st.text_input(
    "Search TransactionID"
)

if search:

    result = filtered_df[
        filtered_df['TransactionID']
        .astype(str)
        == search
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

else:

    st.dataframe(
        filtered_df.head(200),
        use_container_width=True
    )

st.divider()

# Scatter Plot
fig = px.scatter(
    filtered_df,
    x='HourOfDay',
    y='TransactionAmt',
    color='RiskTier',
    size='FraudProbability',
    hover_data=['TransactionID'],
    title='Fraud Risk Analysis'
)

fig.update_layout(
    paper_bgcolor='#0E1117',
    plot_bgcolor='#0E1117',
    font_color='white'
)

st.plotly_chart(
    fig,
    use_container_width=True
)