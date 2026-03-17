# 🎵 Spotify Music Recommender

A **supervised machine learning** system that predicts whether a user will **like or dislike** a song based on its Spotify audio features. The best-performing model is deployed as a live Streamlit web app.

---

## 🚀 Live Demo

**Try it now →** [songs-recommender-by-aditya.streamlit.app](https://songs-recommender-by-aditya.streamlit.app/)

<img width="3644" height="2570" alt="songs-recommender-by-aditya streamlit app_" src="https://github.com/user-attachments/assets/9493cde9-6f7c-439b-8e45-09db025688fb" />


> Enter any song's audio features and get an instant prediction on whether you'd like it.

---



## 📖 Overview

This project uses Spotify audio features to build a **binary classification model** that predicts song preference (`liked = 1` or `not liked = 0`). Five ensemble classifiers were trained and benchmarked. The **Extra Trees Classifier** was selected as the final model, saved to `spotify-recommender.pkl`, and deployed via Streamlit.

---

## ✨ Features

- 🎧 Predicts song preference (liked / not liked) from 13 Spotify audio features
- 🤖 5 ensemble ML models trained and evaluated head-to-head
- 📊 Full EDA with null-value checks and class balance analysis
- 🌐 Live Streamlit app — no setup required
- 💾 Pre-trained model (`.pkl`) for fast local inference
- 📓 Jupyter Notebook with the complete ML pipeline

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.13 |
| Data / EDA | Pandas, NumPy, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, LightGBM |
| Model Serialization | Joblib (`.pkl`) |
| Web App | Streamlit |
| Deployment | Streamlit Community Cloud |
| Dataset | Spotify tracks (`data.csv`) |

---

## 📁 Project Structure

```
Song-preference/
│
├── .devcontainer/                   # Dev container configuration
│
├── Spotify Music Recommender.ipynb  # Full ML pipeline: EDA → training → evaluation
├── app.py                           # Streamlit app — input UI and prediction logic
├── Flask_run.py                     # Alternative Flask entry point
├── data.csv                         # Spotify tracks dataset (195 records, 14 columns)
├── spotify-recommender.pkl          # Saved Extra Trees Classifier model (joblib)
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

---

## 📊 Dataset

The dataset (`data.csv`) contains **195 Spotify tracks** with the following audio features:

| Feature | Description |
|---|---|
| `danceability` | How suitable a track is for dancing (0.0 – 1.0) |
| `energy` | Intensity and activity of the track (0.0 – 1.0) |
| `key` | Musical key of the track (0 – 11) |
| `loudness` | Overall loudness in decibels |
| `mode` | Modality — major (1) or minor (0) |
| `speechiness` | Presence of spoken words (0.0 – 1.0) |
| `acousticness` | Confidence that the track is acoustic (0.0 – 1.0) |
| `instrumentalness` | Predicts whether a track has no vocals (0.0 – 1.0) |
| `liveness` | Presence of a live audience (0.0 – 1.0) |
| `valence` | Musical positiveness of the track (0.0 – 1.0) |
| `tempo` | Estimated tempo in BPM |
| `duration_ms` | Duration of the track in milliseconds |
| `time_signature` | Estimated time signature (1 – 5) |
| `liked` | **Target variable** — 1 (liked) or 0 (not liked) |

**Class distribution:** 100 liked songs vs. 95 not liked — well balanced, no resampling required.  
**No missing values** found across all 195 records.

---

## 🧠 ML Pipeline

### Data Preprocessing

- Features (`X`): all columns except `liked`
- Target (`y`): `liked` column
- Train/test split: **70% training (136 samples) / 30% testing (59 samples)**
- No scaling applied — tree-based models used throughout

### Models Trained

Five ensemble classifiers were trained and compared:

1. **Random Forest Classifier** (`RandomForestClassifier`)
2. **Extra Trees Classifier** (`ExtraTreesClassifier`)
3. **Bagging Classifier** (`BaggingClassifier`, n_estimators=100)
4. **AdaBoost Classifier** (`AdaBoostClassifier`, n_estimators=100)
5. **LightGBM Classifier** (`LGBMClassifier`)

### Model Performance

| Model | Accuracy | ROC AUC |
|---|---|---|
| Random Forest | 94.92% | 0.9440 |
| Extra Trees | 94.92% | 0.9440 |
| Bagging Classifier | 91.53% | 0.9155 |
| AdaBoost ⭐ | **96.61%** | **0.9649** |
| LightGBM | Trained | Evaluated |

> Confusion matrices were generated for all models to visualise true/false positives and negatives.

### Best Model

The **Extra Trees Classifier** (`extraTree_clf`) was selected as the final deployed model:

```python
from joblib import dump
dump(extraTree_clf, "spotify-recommender.pkl")
```

> Although AdaBoost achieved the highest accuracy on the test split (96.61%), the Extra Trees model was chosen for deployment for its speed, robustness to overfitting, and nearly equivalent ROC AUC score.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/Adityax-94/Song-preference.git
cd Song-preference
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### Running Locally

**Streamlit app:**

```bash
streamlit run app.py
```

**Flask app:**

```bash
python Flask_run.py
```

Then open your browser and navigate to:

```
http://localhost:8501   # Streamlit
http://127.0.0.1:5000  # Flask
```

### Re-running the Notebook

To explore the data or retrain models:

```bash
jupyter notebook "Spotify Music Recommender.ipynb"
```

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Aditya** — [@Adityax-94](https://github.com/Adityax-94)

---

> ⭐ If you found this project helpful, please give it a star on GitHub!
