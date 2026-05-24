import streamlit as st

st.set_page_config(
    page_title="Fraud Detection AI",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1,h2,h3 {
    color: white;
}

[data-testid="metric-container"] {
    background-color: #1E1E1E;
    border: 1px solid #333333;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

st.title("💳 AI Fraud Detection System")

st.markdown("""
### Real-Time Fraud Monitoring & Explainable AI Dashboard
""")

st.image(
    "https://www.bluefin.com/wp-content/uploads/2026/03/How-to-Detect-Fraud-Transactions.jpg",
    use_container_width=True
)

st.sidebar.success("Select a page above")