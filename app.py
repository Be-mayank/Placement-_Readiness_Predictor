import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(page_title="Placement Readiness Predictor", page_icon="🎓")
st.title("🎓 Placement Readiness Predictor")

MODEL_PATH = Path("placement_readiness_model.joblib")

if not MODEL_PATH.exists():
    st.error("Run the notebook first to create placement_readiness_model.joblib.")
    st.stop()

model = joblib.load(MODEL_PATH)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", 15, 60, 21)
course = st.text_input("Course", "B.Tech")
branch = st.text_input("Branch", "CSE")
year = st.number_input("Year", 1, 6, 4)
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.5, 0.1)
backlogs = st.number_input("Backlogs", 0, 20, 0)
projects = st.number_input("Projects", 0, 20, 2)

tech_skill = st.slider("Technical Skill", 0, 10, 7)
comm_skill = st.slider("Communication Skill", 0, 10, 7)
apt_skill = st.slider("Aptitude Skill", 0, 10, 7)
team_skill = st.slider("Team Skill", 0, 10, 7)

participation = st.selectbox("Participation", ["Yes", "No"])
internship = st.selectbox("Internship", ["Yes", "No"])
training = st.selectbox("Training", ["Yes", "No"])

languages = st.text_input("Languages (semicolon-separated)", "Python;Java")
certifications = st.text_input("Certifications (semicolon-separated)", "AI/ML")

def contains(text, item):
    return int(item.lower() in text.lower())

def make_input():
    return pd.DataFrame([{
        "gender": gender, "age": age, "course": course, "branch": branch,
        "year": year, "cgpa": cgpa, "backlogs": backlogs, "projects": projects,
        "tech_skill": tech_skill, "comm_skill": comm_skill,
        "apt_skill": apt_skill, "team_skill": team_skill,
        "participation": participation, "internship": internship,
        "training": training,
        "language_count": len([x for x in languages.split(";") if x.strip()]),
        "has_python": contains(languages, "Python"),
        "has_java": contains(languages, "Java"),
        "has_cplusplus": contains(languages, "C++"),
        "has_c": contains(languages, "C"),
        "has_javascript": contains(languages, "JavaScript"),
        "certification_count": len([x for x in certifications.split(";") if x.strip()]),
        "cert_ai_ml": contains(certifications, "AI/ML"),
        "cert_data_analytics": contains(certifications, "Data Analytics"),
        "cert_cloud_computing": contains(certifications, "Cloud Computing"),
        "cert_cyber_security": contains(certifications, "Cyber Security")
    }])

if st.button("Predict Placement"):
    x = make_input()
    pred = int(model.predict(x)[0])
    label = "Placed" if pred == 1 else "Not Placed"
    st.success(f"Predicted result: **{label}**")
    if hasattr(model, "predict_proba"):
        p = float(model.predict_proba(x)[0, 1])
        st.metric("Probability of Placed", f"{p:.2%}")
    st.caption("This is a model-based estimate, not a guarantee of placement.")
