Spotify Music Recommender
A machine learning project that predicts whether users will like Spotify songs based on audio features. The best model, ExtraTreesClassifier, achieves 94.9% accuracy and 0.944 ROC AUC on test data.

Features
Analyzes 13 Spotify audio features like danceability, energy, and valence.
​

Compares Decision Tree, Random Forest, ExtraTrees, Bagging, AdaBoost, and LightGBM classifiers.
​

Includes EDA with correlation heatmap, confusion matrices, and model evaluation.

Saves the top-performing model for inference.

Dataset
The dataset contains 195 Spotify tracks with these columns:
​

Feature	Description
danceability	Suitability for dancing (0.0 to 1.0).
energy	Perceptual measure of intensity (0.0 to 1.0).
key	Key of the track (0 to 11).
loudness	Loudness in dB (-60 to 0).
mode	Modality (0: minor, 1: major).
speechiness	Presence of spoken words (0.0 to 1.0).
acousticness	Acoustic confidence (0.0 to 1.0).
instrumentalness	Likelihood of no vocals (0.0 to 1.0).
liveness	Likelihood of live recording (0.0 to 1.0).
valence	Musical positivity (0.0 to 1.0).
tempo	Beats per minute.
duration_ms	Track length in milliseconds.
time_signature	Beats per bar (3 to 7).
liked	Target: 1 if liked, 0 otherwise (100 positive, 95 negative).
No missing values; balanced classes.

Results
Model performance on 30% test set (59 samples):
​

Model	Accuracy	ROC AUC
Decision Tree	0.881	0.900
Random Forest	0.949	0.944
ExtraTrees	0.949	0.944
Bagging	0.915	0.915
AdaBoost	0.966	0.965
LightGBM	0.932	0.930
ExtraTreesClassifier selected as best; saved as spotify-recommender.pkl.

Quick Start
Clone repo and install dependencies:

text
pip install pandas numpy scikit-learn lightgbm seaborn matplotlib joblib
Load data (data.csv) and train/test split (70/30).

Run notebook for EDA and models.

Load saved model:

python
from joblib import load
model = load('spotify-recommender.pkl')
prediction = model.predict([[0.8, 0.6, 7, -6.7, 0, 0.05, 0.45, 0.0007, 0.1, 0.63, 96, 304524, 4]])
Usage
Predict likes for new tracks:

python
import pandas as pd
new_track = pd.DataFrame({...})  # 13 features
print("Liked:" if model.predict(new_track)[0] else "Not liked")
Project Structure
text
├── data.csv              # Spotify dataset
├── spotify-recommender.ipynb  # Main notebook
└── spotify-recommender.pkl   # Saved model
Contributing
Fork, create branch, PR improvements like hyperparameter tuning or new features.

License
MIT License.
​

give me a readme.md file to upload on git hub
text
# Spotify Music Recommender 🎵

**By: Soorya Parthiban**

A machine learning project that predicts whether users will like Spotify songs based on 13 audio features. The ExtraTreesClassifier achieves **94.9% accuracy** and **0.944 ROC AUC** on test data.

![Spotify](https://img.shields.io/badge/Spotify-Music%20Recommender-brightgreen?style=flat&logo=spotify&logoColor=white) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat&logo=python) ![Accuracy](https://img.shields.io/badge/Accuracy-94.9%25-orange?style=flat)

## 📊 Project Overview

This project builds a binary classifier to predict if a Spotify track will be "liked" (1) or "not liked" (0) using audio features like danceability, energy, valence, tempo, and more. Multiple ML models were compared, with ensemble methods performing best.

**Dataset**: 195 tracks (100 liked, 95 not liked) with zero missing values.

## 🎯 Key Results

| Model | Accuracy | ROC AUC |
|-------|----------|---------|
| **ExtraTrees** | **0.949** | **0.944** |
| Random Forest | 0.949 | 0.944 |
| **AdaBoost** | **0.966** | **0.965** |
| LightGBM | 0.932 | 0.930 |
| Bagging | 0.915 | 0.915 |
| Decision Tree | 0.881 | 0.900 |

**Best Model**: `ExtraTreesClassifier` saved as `spotify-recommender.pkl`

## 📈 Audio Features Analyzed

| Feature | Description | Range |
|---------|-------------|-------|
| `danceability` | Dance suitability | 0.0-1.0 |
| `energy` | Intensity & activity | 0.0-1.0 |
| `loudness` | Volume in dB | -60 to 0 |
| `valence` | Musical positivity | 0.0-1.0 |
| `acousticness` | Acoustic confidence | 0.0-1.0 |
| `tempo` | BPM | 60-180+ |
| `duration_ms` | Track length | ms |

**Full list**: 13 features total + `liked` target

## 🚀 Quick Start

### 1. Clone & Setup
```bash
git clone <your-repo-url>
cd spotify-music-recommender
pip install -r requirements.txt
2. Required Dependencies
text
pandas
numpy
scikit-learn
lightgbm
seaborn
matplotlib
joblib
3. Run the Analysis
bash
jupyter notebook spotify-recommender.ipynb
4. Load Saved Model
python
from joblib import load
model = load('spotify-recommender.pkl')

# Predict single track (13 features required)
new_track = [[0.8, 0.6, 7, -6.7, 0, 0.05, 0.45, 0.0007, 0.1, 0.63, 96, 304524, 4]]
prediction = model.predict(new_track)
print("Liked!" if prediction == 1 else "Not liked")
🗂️ Project Structure
text
├── data.csv                    # Spotify dataset (195 tracks)
├── spotify-recommender.ipynb   # Main analysis notebook
├── spotify-recommender.pkl     # Trained ExtraTrees model
├── requirements.txt           # Dependencies
└── README.md                 # This file
📊 Data Insights
Train/Test Split: 70% / 30% (136 train, 59 test)

Class Balance: 100 liked (51%), 95 not liked (49%)

Correlation Heatmap: Available in notebook

Confusion Matrices: Generated for all models

🔮 Future Improvements
 Hyperparameter tuning with GridSearchCV

 Cross-validation for robust evaluation

 Feature importance analysis & selection

 Real-time Spotify API integration

 Web app deployment (Streamlit/Flask)

 Larger dataset training

📝 Usage Example
python
import pandas as pd
from joblib import load

model = load('spotify-recommender.pkl')

# New track features (must match training order)
track_features = pd.DataFrame({
    'danceability': [0.803], 'energy': [0.624], 'key':,[11]
    'loudness': [-6.764], 'mode': , 'speechiness': [0.0477],
    # ... 8 more features
})

prediction = model.predict(track_features)
print(f"Will you like this track? {'Yes' if prediction == 1 else 'No'}")
🤝 Contributing
Fork the repository

Create feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add some AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Soorya Parthiban - Project Creator

Spotify for providing audio features data

Scikit-learn, LightGBM, and ensemble method authors

⭐ Star this repo if you found it helpful! ⭐

text

**Just copy-paste this entire file as `README.md` to your GitHub repository root!** 

This README includes:
- ✅ Professional badges & formatting
- ✅ Model performance table
- ✅ Installation & usage instructions  
- ✅ Project structure
- ✅ Feature descriptions
- ✅ Future improvements roadmap
- ✅ Contributing guidelines
- ✅ All technical details from your notebook

Perfect for showcasing your ML project! 🚀
