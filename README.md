# 📰 Fake News Detector

A Machine Learning project to classify news articles as **Fake** or **Real** using Logistic Regression and TF-IDF Vectorization.  
The project includes a **Streamlit web app** for interactive predictions.

---

## 🚀 Features
- Preprocessing of text data (cleaning, stopword removal, vectorization).
- Machine learning model using **Logistic Regression**.
- Web interface built with **Streamlit**.
- Predict whether a given news headline or article is *Fake* or *Real*.

---

## 📂 Project Structure
fake-news-detector/
│── app.py # Streamlit web app
│── vectorizer.jb # Saved TF-IDF vectorizer
│── lr_model.jb # Trained Logistic Regression model
│── requirements.txt # Python dependencies
│── Fake.csv # (not uploaded - see Dataset section)
│── True.csv # (not uploaded - see Dataset section)
│── README.md

---

## 📊 Dataset
The dataset is not included in this repository because of its large size.  
Download it from Kaggle:

👉 [Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

Place `Fake.csv` and `True.csv` in the project folder before running training.

---

## ⚙️ Installation

Clone this repository:
```bash
git clone https://github.com/YOUR-USERNAME/fake-news-detector.git
cd fake-news-detector.

Install dependencies:

pip install -r requirements.txt
```
---

## ▶️ Usage

Run the Streamlit app:

python -m streamlit run app.py

---

## 🛠️ Tech Stack

Python 🐍

Pandas, Scikit-learn, Joblib

Streamlit

TF-IDF Vectorization + Logistic Regression

## 📌 Future Improvements

Add more ML models (Naive Bayes, SVM, Deep Learning).

Improve preprocessing with advanced NLP techniques.

Deploy on Streamlit Cloud or Heroku.

## 👩‍💻 Author

Muskan Verma
AI/ML Engineer | B.Tech Student
