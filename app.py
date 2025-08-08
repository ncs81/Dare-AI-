st.set_page_config(page_title="project D.A.R.E. , Be aware Be secure.")

st.title("Drug Awareness And Risk Estimator")
st.subheader("AI Based Assistant")

st.markdown("---")

st.header("Learn About Drugs : Most Used Substances Among Today's Gen Z")
drug list={"Nicotine and Vaping"="Vaping is often perceived as less harmful than traditional smoking, which may explain its popularity among Gen Z. However, the high concentration of nicotine found in many vaping products can lead to addiction, cognitive impairment, and respiratory issues.",
"Cannabis Use"="Cannabis (marijuana) remains one of the most commonly used substances among Gen Z, with a growing number of states legalizing its recreational use.While cannabis is often seen as a “safe” or “natural” drug, high-potency products and the frequent use of edibles and vapes can lead to increased risk of dependency, mental health issues (such as anxiety and psychosis), and cognitive impairments, especially for younger users whose brains are still developing.",
"Prescription Drug Misuse"="Prescription drug misuse, particularly of opioids, benzodiazepines (such as Xanax), and stimulants (such as Adderall), is another concerning trend among Gen Z. Many young adults turn to prescription drugs for self-medication—using stimulants to cope with academic pressure or anxiety, or opioids and benzodiazepines to manage stress or trauma.",
"Alcohol Use"="Although alcohol use has declined somewhat among Gen Z compared to previous generations, it remains one of the most widely abused substances. Data from the Centers for Disease Control and Prevention (CDC) shows that binge drinking is still a major concern, particularly among college students and young adults in social settings.",
"Polysubstance Use"="A growing concern among substance use trends for Gen Z is the rise in polysubstance use—using more than one substance simultaneously or in close succession. This can involve mixing alcohol with cannabis, prescription drugs, or other substances, leading to dangerous interactions and an increased risk of overdose."}

selected_drug=select.selecbox("select a drug to learn more :,list(drug_list.keys()))
                              if selected drug:st.info(druglist_[selected_drug])

st.markdown(---)
                              
st.header("Addiction Risk Reader")
            
st.write("Ans a few questions to check your risk level:")
            
