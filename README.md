# 🧠 AI Doctor - Disease & Medicine Predictor using Symptoms (ML + NLP)

A smart AI-based Doctor that predicts the most probable **disease** based on user-reported **symptoms** and recommends **medicines** including:
- 💊 English Allopathy
- 🌿 Ayurvedic Medicines
- 🍽️ Diet Suggestions
- 🏋️‍♀️ Workout Recommendations

Built using **Machine Learning** and **Natural Language Processing (NLP)** with a clean, user-friendly web interface.

---

## 🚀 Features

- ✅ Predicts Disease from given symptoms
- 💊 Recommends English (Allopathy) and Ayurvedic Medicines
- 🍽️ Provides Diet Plans and 🏋️ Exercise Tips
- 🧾 Generates downloadable **PDF report**
- 🌐 Built with Flask Web App (Beginner to Advanced Level)
- 📊 Clean dataset with 100+ diseases and symptoms

---

## 🧠 How It Works

### Input:
- A list of symptoms from the user

### Backend Process:
1. Preprocesses symptoms
2. Predicts disease using a trained machine learning model
3. Maps predictions to:
   - English medicines
   - Ayurvedic alternatives
   - Suggested diet & workout
4. Optionally, creates a **PDF report** for the user

---

## 📂 Project Structure

ai-doctor/ ├── templates/ # HTML templates │ └── index.html # Frontend interface ├── static/ # CSS, JS, images ├── model/ # Trained ML model ├── disease_data.csv # Dataset: symptoms, disease, medicine ├── app.py # Flask backend ├── predictor.py # Core logic: prediction, recommendation ├── pdf_generator.py # PDF creation ├── requirements.txt └── README.md


---

## 🛠 Tech Stack

- **Python 3.9+**
- **Flask** – Web framework
- **Pandas / NumPy** – Data handling
- **Scikit-learn** – ML model (RandomForest / DecisionTree)
- **FPDF / ReportLab** – PDF generation
- **HTML/CSS** – Frontend interface

---

## 🧪 Sample Demo

### Input:

### Output:
- **Disease Predicted**: Viral Infection
- **English Medicine**: Paracetamol, Azithromycin
- **Ayurvedic Medicine**: Giloy, Tulsi drops
- **Diet**: Light food, warm water
- **Workout**: Rest, light stretching
- ✅ [Download PDF Report]

---

## 📥 Installation

```bash
git clone https://github.com/yourusername/ai-doctor.git
cd ai-doctor
pip install -r requirements.txt
python app.py
