# 📧 Spam Email Classifier

A machine learning web application that detects whether a given message is **spam** or **not spam**, complete with a confidence score. Built with Python, scikit-learn, and Streamlit.

---

## 🚀 Demo

Enter any email or SMS message into the app and instantly get a prediction:

- ✅ **Not Spam** — with confidence percentage
- 🚨 **Spam** — with confidence percentage

---

## 🧠 How It Works

1. The raw text message is transformed using a pre-trained **TF-IDF Vectorizer** (`vectorizer.pkl`).
2. The vectorized input is passed to a trained **classification model** (`model.pkl`).
3. The model predicts whether the message is spam (`1`) or not spam (`0`), along with a probability score.

---

## 🗂️ Project Structure

```
spam-email-classifier/
│
├── app.py              # Streamlit web application
├── model.py            # Model training script
├── model.pkl           # Trained classification model (serialized)
├── vectorizer.pkl      # Fitted TF-IDF vectorizer (serialized)
├── spam.csv            # Dataset used for training
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🛠️ Tech Stack

| Layer        | Technology                          |
|--------------|-------------------------------------|
| Language     | Python 3.x                          |
| ML Library   | scikit-learn                        |
| Web UI       | Streamlit                           |
| Data         | pandas, numpy                       |
| Dataset      | SMS/Email spam dataset (`spam.csv`) |

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/SampratiSinha/spam-email-classifier.git
cd spam-email-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

---

## 📊 Dataset

The model is trained on `spam.csv`, a classic SMS spam collection dataset containing labeled messages categorized as either `spam` or `ham` (not spam).

---

## 🔁 Retraining the Model

To retrain the model on new data, run:

```bash
python model.py
```

This will regenerate `model.pkl` and `vectorizer.pkl`.

---

## 📦 Dependencies

```
streamlit
scikit-learn
pandas
numpy
```

Install all at once with:

```bash
pip install -r requirements.txt
```

---

## 🙋 Author

**Samprati Sinha**  
[GitHub Profile](https://github.com/SampratiSinha)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
