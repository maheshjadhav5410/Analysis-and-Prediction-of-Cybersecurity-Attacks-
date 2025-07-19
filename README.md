
# 🔐 Analysis and Prediction of Cybersecurity Attacks

A machine learning-powered web application developed using Python, Django, and Scikit-learn to analyze and predict the severity of cybersecurity attacks based on real-time network traffic data.

---

## 📌 Project Highlights

- 📊 Performed detailed **analysis of network traffic** to detect cyber threats
- 🤖 Implemented **machine learning models** to predict attack severity (Low, Medium, High)
- 🌐 Built an interactive **web interface using Django and Streamlit**
- 📈 Visualized attack patterns and severity distributions using Matplotlib and Seaborn
- 🧠 Used **GradientBoostingClassifier** for accurate severity prediction

---

## 🧠 Problem Statement

Modern networks face thousands of cyber threats daily. Detecting these threats and understanding their severity in real-time is crucial for effective response. This project helps security teams by:

- Predicting **threat severity levels**
- Identifying **types of attacks**
- Visualizing patterns in traffic that indicate **potential breaches**

---

## 🛠️ Tech Stack

| Category       | Technologies Used                          |
|----------------|---------------------------------------------|
| Programming    | Python                                      |
| Frameworks     | Django (Web), Streamlit (ML Interface)      |
| ML Libraries   | Scikit-learn, Pandas, NumPy, Seaborn, Matplotlib |
| Frontend       | HTML, CSS, JavaScript                       |
| Database       | SQLite (via Django ORM)                     |
| Tools          | VS Code, Jupyter Notebooks                  |

---

## 🧩 Dataset Features

> Sample fields from the dataset used:

- `Timestamp`
- `Source IP`, `Destination IP`
- `Protocol`, `Packet Length`, `Anomaly Score`
- `Attack Type`, `Severity Level`
- `Firewall Logs`, `IDS Alerts`
- `Geo-location`, `Network Segment`

> Target Column: `Severity Level` (Low, Medium, High)

---

## 🔍 Workflow / Pipeline

```plaintext
[Raw Network Data]
       ↓
[Data Preprocessing with Pandas]
       ↓
[Feature Selection & Label Encoding]
       ↓
[Model Training using GradientBoostingClassifier]
       ↓
[Evaluation: Accuracy, Confusion Matrix]
       ↓
[Deployment with Streamlit + Django Interface]

⚙️ Key Features
✅ Machine Learning
Data cleaning, feature extraction, and transformation

Trained Gradient Boosting Classifier with ~85% accuracy

Used Scikit-learn pipeline for training and evaluation

✅ Data Visualization
Severity distribution (Low, Medium, High)

Attack type heatmap

Real-time prediction interface using Streamlit

✅ Web Interface
Upload file or input features manually

View predictions and graphs instantly

Django-based admin panel to manage datasets

🚀 How to Run the Project Locally
# Clone the repo
git clone https://github.com/your-username/Analysis-and-Prediction-of-Cybersecurity-Attacks-.git
cd cyberthreat

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver

# For ML Streamlit app
cd ml_interface/
streamlit run app.py

📁 Folder Structure (Example)
cyberthreat/
├── ml_model/
│   ├── model.pkl
│   ├── preprocessing.py
│   └── app.py  # Streamlit
├── predictor_app/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── db.sqlite3
├── manage.py
└── requirements.txt


