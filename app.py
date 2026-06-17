
# app.py
import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import gradio as gr
import faiss
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from sklearn.feature_extraction.text import TfidfVectorizer

DATASET_FOLDER = r"C:\Users\bhard\indian_drug_interaction_dataset"
INTERACTION_FILE = os.path.join(DATASET_FOLDER, "interactions.csv")
DRUG_INFO_FILE = os.path.join(DATASET_FOLDER, "drug_info.csv")
SIDE_EFFECT_FILE = os.path.join(DATASET_FOLDER, "side_effects.csv")

interaction_df = pd.read_csv(INTERACTION_FILE).fillna("")
drug_df = pd.read_csv(DRUG_INFO_FILE).fillna("")
side_df = pd.read_csv(SIDE_EFFECT_FILE).fillna("")

documents = []
for _, row in interaction_df.iterrows():
    documents.append(
        f"Drug A:{row['drug_a']} | Drug B:{row['drug_b']} | "
        f"Severity:{row['severity']} | Description:{row['description']} | "
        f"Recommendation:{row['recommendation']}"
    )

vectorizer = TfidfVectorizer()
embeddings = vectorizer.fit_transform(documents).toarray().astype("float32")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

history=[]

def retrieve(query,k=5):
    q = vectorizer.transform([query]).toarray().astype("float32")
    _, idx = index.search(q, min(k,len(documents)))
    return [documents[i] for i in idx[0]]

def get_drug_info(name):
    rows = drug_df[drug_df["drug_name"].astype(str).str.lower()==name.lower()]
    if rows.empty:
        return {"Category":"Unknown","Uses":"Unknown"}
    r=rows.iloc[0]
    return {
        "Category":r.get("category","Unknown"),
        "Uses":r.get("uses","Unknown")
    }

def get_side(name):
    rows=side_df[side_df["drug_name"].astype(str).str.lower()==name.lower()]
    if rows.empty:
        return "Unknown"
    return ", ".join(rows["side_effect"].astype(str))

def risk_score(text):
    t=text.lower()
    if "contra" in t or "critical" in t:
        return 95
    if "high" in t:
        return 82
    if "moderate" in t:
        return 55
    return 15

def gauge(score):
    fig=go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        title={"text":"Risk Score"},
        gauge={"axis":{"range":[0,100]}}
    ))
    return fig

def pie(score):
    if score>80:
        vals=[80,15,5]
    elif score>40:
        vals=[25,60,15]
    else:
        vals=[5,20,75]
    fig=plt.figure(figsize=(4,4))
    plt.pie(vals,labels=["High","Moderate","Low"],autopct="%1.0f%%")
    return fig

def analyze(inp):
    if not inp.strip():
        return "Enter drugs", None, None, pd.DataFrame()
    docs=retrieve(inp)
    score=risk_score(" ".join(docs))
    risk="🟢 LOW"
    if score>=80:risk="🔴 HIGH"
    elif score>=40:risk="🟠 MODERATE"

    report=f"# 💊 MediGuard AI Report\n\n## Overall Risk: {risk}\n### Score: {score}/100\n\n"
    report+="## Retrieved Interactions\n"
    for d in docs:
        report+=f"- {d}\n"
    report+="\n## Drug Details\n"
    rows=[]
    for d in [x.strip() for x in inp.split(",")]:
        info=get_drug_info(d)
        side=get_side(d)
        rows.append([d,info["Category"],info["Uses"],side])
        report+=f"\n### {d}\n- Category: {info['Category']}\n- Uses: {info['Uses']}\n- Side Effects: {side}\n"
    report+="\n## AI Summary\n"
    report+="The entered medicines were compared with the interaction database using TF-IDF + FAISS retrieval. Please consult a physician before changing medication."
    history.append(inp)
    df=pd.DataFrame(rows,columns=["Drug","Category","Uses","Side Effects"])
    return report,gauge(score),pie(score),df

theme=gr.themes.Soft()

with gr.Blocks(theme=theme,title="MediGuard AI") as demo:
    gr.Markdown("# 💊 MediGuard AI\n### Drug Interaction Safety Assistant")
    with gr.Tab("Analysis"):
        inp=gr.Textbox(label="Drugs",placeholder="Warfarin, Aspirin")
        btn=gr.Button("Analyze",variant="primary")
        md=gr.Markdown()
        with gr.Row():
            gauge_plot=gr.Plot()
            pie_plot=gr.Plot()
        table=gr.Dataframe()
        btn.click(analyze,inp,[md,gauge_plot,pie_plot,table])
    with gr.Tab("About"):
        gr.Markdown("""
### Features
- TF-IDF Retrieval
- FAISS Index
- Drug Information
- Side Effects
- Risk Score
- Plotly Gauge
- Matplotlib Pie Chart
- Gradio Dashboard
""")

if __name__=="__main__":
    demo.launch()
