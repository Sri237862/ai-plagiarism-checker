import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
import nltk
import PyPDF2
import docx
import matplotlib.pyplot as plt

nltk.download('punkt', quiet=True)

st.title("AI Plagiarism Checker with Visualization")

# ---------- File Reading ----------

def read_txt(file):
    return file.read().decode("utf-8")

def read_pdf(file):
    pdf = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

def extract_text(file):
    if file.type == "text/plain":
        return read_txt(file)
    elif file.type == "application/pdf":
        return read_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return read_docx(file)
    else:
        return ""


# ---------- Text Input ----------

st.subheader("Enter Text")

text1 = st.text_area("Text 1")
text2 = st.text_area("Text 2")


# ---------- File Upload ----------

st.subheader("Or Upload Files")

file1 = st.file_uploader("Upload Document 1", type=["txt","pdf","docx"])
file2 = st.file_uploader("Upload Document 2", type=["txt","pdf","docx"])


# ---------- Similarity ----------

def calculate_similarity(t1, t2):

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([t1, t2])
    similarity = cosine_similarity(vectors)

    return similarity[0][1] * 100


# ---------- Sentence Detection ----------

def sentence_similarity(t1, t2):

    s1 = sent_tokenize(t1)
    s2 = sent_tokenize(t2)

    copied = []

    for a in s1:
        for b in s2:

            if not a.strip() or not b.strip():
                continue

            try:
                vectorizer = TfidfVectorizer().fit_transform([a, b])
                sim = cosine_similarity(vectorizer)[0][1]

                if sim > 0.6:
                    copied.append(a)

            except:
                continue

    return copied


# ---------- Visualization ----------

def similarity_chart(score):

    labels = ['Similarity', 'Unique']
    values = [score, 100-score]

    fig, ax = plt.subplots()

    ax.bar(labels, values)

    ax.set_ylabel("Percentage")
    ax.set_title("Plagiarism Analysis")

    st.pyplot(fig)


# ---------- Check Button ----------

if st.button("Check Plagiarism"):

    if file1 and file2:
        text1 = extract_text(file1)
        text2 = extract_text(file2)

    if text1 == "" or text2 == "":
        st.warning("Please enter text or upload files")

    else:

        score = calculate_similarity(text1, text2)

        st.subheader(f"Similarity Score: {score:.2f}%")

        st.progress(int(score))

        similarity_chart(score)

        if score > 70:
            st.error("High Plagiarism Detected")
        elif score > 40:
            st.warning("Moderate Similarity")
        else:
            st.success("Low Similarity")

        st.subheader("Copied Sentences")

        copied = sentence_similarity(text1, text2)

        if copied:

            for sentence in copied:
                st.markdown(f"<span style='color:red'>{sentence}</span>", unsafe_allow_html=True)

        else:
            st.write("No copied sentences detected")