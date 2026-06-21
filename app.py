import streamlit as st
import pandas as pd
import plotly.express as px

from utils.portfolio import get_portfolio
from utils.risk import get_risk_score
from utils.recommendation import get_return

st.set_page_config(
    page_title="Investment Insight Dashboard",
    layout="wide"
)

st.title("AI-Powered Investment Insight Dashboard")

st.sidebar.header("Investor Profile")

age = st.sidebar.slider(
    "Age",
    18,
    80,
    25
)

goal = st.sidebar.selectbox(
    "Investment Goal",
    [
        "Wealth Creation",
        "Retirement Planning",
        "Child Education",
        "House Purchase",
        "Emergency Fund"
    ]
)

period = st.sidebar.number_input(
    "Investment Period (Years)",
    min_value=1,
    value=10
)

risk = st.sidebar.selectbox(
    "Risk Appetite",
    [
        "Conservative",
        "Moderate",
        "Aggressive"
    ]
)

if period < 3:
    st.error(
        "Investment period must be at least 3 years"
    )
    st.stop()

portfolio = get_portfolio(risk)

df = pd.DataFrame(
    portfolio.items(),
    columns=["Asset","Allocation"]
)

expected_return = get_return(risk)

risk_score = get_risk_score(risk)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Expected Return",
    expected_return
)

c2.metric(
    "Risk Score",
    f"{risk_score}/10"
)

c3.metric(
    "Investment Period",
    f"{period} Years"
)

fig = px.pie(
    df,
    names="Asset",
    values="Allocation",
    title="Portfolio Diversification"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader(
    "Asset Allocation"
)

st.dataframe(df)

st.subheader(
    "Investment Summary"
)

st.write(
    f"""
    Age: {age}

    Goal: {goal}

    Risk Appetite: {risk}

    Investment Period: {period} years

    Expected Return: {expected_return}
    """
)

st.subheader(
    "Personalized Recommendation"
)

if risk == "Conservative":
    st.success(
        "Focus on capital protection using bonds, debt funds and fixed deposits."
    )

elif risk == "Moderate":
    st.info(
        "Balanced approach combining growth and stability."
    )

else:
    st.warning(
        "Growth-focused strategy with higher volatility and long-term wealth creation."
    )
