# AI Plagiarism Checker 🔍

An AI-powered web application that detects plagiarism between two pieces of text or documents using Natural Language Processing (NLP).

The system calculates similarity using **TF-IDF vectorization** and **Cosine Similarity**, highlights copied sentences, and shows a visual similarity chart.

---

## 🌐 Live Demo

Try the application here:

https://ai-plagiarism-checker-hg7v.onrender.com

---

## 🚀 Features

* Compare **two texts for plagiarism**
* Upload **TXT, PDF, or DOCX files**
* Calculate **similarity percentage**
* Detect and display **copied sentences**
* **Visualization chart** for plagiarism analysis
* Interactive **Streamlit web interface**

---

## 🧠 Technologies Used

* Python
* Streamlit
* Scikit-learn
* NLTK
* PyPDF2
* python-docx
* Matplotlib

These tools help analyze text and compute similarity between documents. Plagiarism checkers typically work by breaking text into smaller units, comparing them with other content, and generating a similarity score. ([Merlin AI][1])

---

## 📂 Project Structure

```
ai-plagiarism-checker
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation (Run Locally)

Clone the repository:

```
git clone https://github.com/Sri237862/ai-plagiarism-checker.git
```

Move into the project directory:

```
cd ai-plagiarism-checker
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
streamlit run app.py
```

Streamlit apps are typically started using the `streamlit run` command, which launches the web interface locally. ([Streamlit Docs][2])

---

## ☁️ Deployment

This project is deployed on **Render**.

Start command used for deployment:

```
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

Binding the app to `0.0.0.0` and using the environment port allows Streamlit apps to run correctly in cloud environments like Render. ([Render][3])

---

## 📊 How It Works

1. User enters text or uploads documents
2. Text is converted into **TF-IDF vectors**
3. **Cosine similarity** calculates similarity score
4. Copied sentences are detected
5. A chart visualizes plagiarism percentage

---

## 💡 Future Improvements

* Semantic plagiarism detection using **transformer models**
* Compare **multiple documents**
* Generate **downloadable plagiarism reports**
* Highlight copied **words inside text**





