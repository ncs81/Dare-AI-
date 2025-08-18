import streamlit as st
from openai import OpenAI
import os

openai_api_key = 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
client = OpenAI(api_key=openai_api_key)

st.set_page_config(page_title="Drug Awareness App", layout="wide")
st.title("💊 Drug Awareness & Support")

st.header("Common Drugs & Their Effects")
drugs = {
    "Cocaine": "A powerful stimulant that can cause addiction, heart problems, and anxiety.",
    "Heroin": "An opioid that is highly addictive and can cause respiratory failure.",
    "LSD": "A hallucinogen that can cause altered thoughts and dangerous behavior.",
    "Methamphetamine": "A stimulant that can damage the brain and cause paranoia."
}

for drug, info in drugs.items():
    st.subheader(drug)
    st.write(info)

st.header("📝 Self-Assessment Quiz")
score = 0
q1 = st.radio("Do you or someone you know use drugs regularly?", ["yes", "no"])
q2 = st.radio("Have you felt the need to cut down?", ["yes", "no"])
q3 = st.radio("Have others expressed concern about your usage?", ["yes", "no"])

if st.button("Check Risk Level"):
    score = sum([q1 == "yes", q2 == "yes", q3 == "yes"])
    if score >= 2:
        st.error("High risk: Please seek help immediately.")
    elif score == 1:
        st.warning("Moderate risk: Monitor and consider talking to a counselor.")
    else:
        st.success("Low risk: Stay informed and healthy.")

st.header("💬 Chat with Drug Awareness Bot")
user_input = st.text_input("Ask me anything about drug safety:")

if user_input:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful drug awareness assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("**Bot:**", response.choices[0].message.content)
    except Exception as e:
        st.error(f"Error: {str(e)}")

st.header("📞 Helpline Numbers")
st.write("- India: 1800-11-0031 (Narcotics Control Bureau)")
st.write("- local helplines : 100 ( police control room )")
