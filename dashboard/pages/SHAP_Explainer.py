import streamlit as st
import pandas as pd

df = pd.read_csv("processed_data.csv")

st.title("🧠 Explainable AI")

transaction_id = st.text_input(
    "Enter TransactionID"
)

if transaction_id:

    result = df[
        df['TransactionID']
        .astype(str)
        == transaction_id
    ]

    st.subheader("Transaction Details")

    st.dataframe(
        result,
        use_container_width=True
    )

    st.divider()

    col1,col2 = st.columns([2,1])

    with col1:

        st.image(
            "charts/Shap_summary.png",
            use_container_width=True
        )

    with col2:

        st.success("""
        Fraud Indicators:

        • High transaction amount

        • Suspicious device usage

        • Abnormal transaction timing

        • Elevated fraud probability
        """)