import streamlit as st
import anthropic

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
        st.success("Low risk: Stay informed and healthy")

# Initialize OpenAI client (key from Streamlit secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💊 Drug Awareness Assistant")
user_input = st.text_input("Ask me anything about drug awareness:")


client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=500,
    messages=[
        {"role": "user", "content": user_input}
    ]
)
st.write("**Bot:**", response.content[0].text)


st.header("📞 Helpline Numbers")
st.write("- India: 1800-11-0031 (Narcotics Control Bureau)")
st.write("- Local helplines: 100 (Police control room)")
