import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from fpdf import FPDF

# Load and train the model
df = pd.read_csv("indian_medicine_dataset_large.csv")
X = df['Symptoms']
y = df[['Disease Name', 'English Medicine Name', 'Ayurvedic Medicine Name', 'Diet Recommendation']]

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))
])
pipeline.fit(X, y)

# Page Config
st.set_page_config(page_title="AI Doctor", page_icon="🩺", layout="centered")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f5f3ff;
        }
        .main {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0,0,0,0.05);
        }
        .title {
            text-align: center;
            background: linear-gradient(90deg, #6366f1, #38bdf8);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            font-size: 2.2rem;
        }
        .input-container {
            margin-top: 2rem;
            padding: 1.5rem;
            border-left: 6px solid #6366f1;
            background-color: #ede9fe;
            border-radius: 8px;
        }
        .result-box {
            margin-top: 1rem;
            padding: 1.5rem;
            border-left: 6px solid #4f46e5;
            background-color: #e0f2fe;
            border-radius: 8px;
        }
        .footer {
            margin-top: 3rem;
            text-align: center;
            font-size: 0.9rem;
            color: #6b7280;
        }
        .stDownloadButton button {
            background-color: #6366f1;
            color: white;
            border-radius: 6px;
            padding: 0.5rem 1rem;
        }
        .stDownloadButton button:hover {
            background-color: #4f46e5;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='title'>🩺 AI Doctor – Get Medical Advice from Your Symptoms</div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin-top: 1rem;'>Describe your symptoms to get a disease prediction, medicines, and diet suggestions.</div>", unsafe_allow_html=True)

# Input
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
symptoms = st.text_input("🔍 Enter your symptoms", placeholder="e.g. headache, sore throat, fatigue, sneezing")
st.markdown("</div>", unsafe_allow_html=True)

if st.button("🔮 Predict"):
    if symptoms.strip() == "":
        st.warning("⚠️ Please enter some symptoms.")
    else:
        prediction = pipeline.predict([symptoms])[0]
        disease, english_medicine, ayurvedic_medicine, diet = prediction

        st.success("✅ Prediction Complete")

        # Display results
        st.markdown("<div class='result-box'>", unsafe_allow_html=True)
        st.subheader("🧾 Predicted Diagnosis")
        st.markdown(f"**📝 Symptoms:** {symptoms}")
        st.markdown(f"**🦠 Disease:** `{disease}`")
        st.markdown(f"**💊 English Medicine:** `{english_medicine}`")
        st.markdown(f"**🌿 Ayurvedic Medicine:** `{ayurvedic_medicine}`")
        st.markdown(f"**🥗 Diet Recommendation:** `{diet}`")
        st.markdown("</div>", unsafe_allow_html=True)

        # PDF generation
        def generate_pdf():
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(33, 37, 41)
            pdf.cell(200, 10, txt="AI Doctor - Medical Report", ln=True, align='C')
            pdf.ln(10)
            pdf.multi_cell(0, 10, f"Symptoms: {symptoms}")
            pdf.multi_cell(0, 10, f"Disease: {disease}")
            pdf.multi_cell(0, 10, f"English Medicine: {english_medicine}")
            pdf.multi_cell(0, 10, f"Ayurvedic Medicine: {ayurvedic_medicine}")
            pdf.multi_cell(0, 10, f"Diet Recommendation: {diet}")
            return pdf.output(dest='S').encode('latin1')

        pdf_data = generate_pdf()
        st.download_button(
            label="📄 Download PDF Report",
            data=pdf_data,
            file_name="AI_Doctor_Report.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown("<div class='footer'>© 2025 AI Doctor | For informational use only. Always consult a certified medical professional.</div>", unsafe_allow_html=True)
