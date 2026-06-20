# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python, Streamlit, and the OMDb API.

This project recommends similar movies based on content similarity using Natural Language Processing (NLP) and cosine similarity.

---
## Live Demo

🚀 Try the app here: https://movie-recommender-by-yash.streamlit.app/


## 🚀 Features

* Search and select a movie from the dataset
* Get top 5 similar movie recommendations
* Movie posters fetched dynamically using OMDb API
* Displays:

  * IMDb Rating ⭐
  * Release Year 📅
  * Genre 🎭
  * Runtime ⏱
* Interactive recommendation flow (click recommended movies to continue exploring)
* Clean and responsive Streamlit UI

---

## 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle
* Requests
* OMDb API

---

## 📂 Project Structure

```bash
movie-recommender-system/
│── app.py
│── movie_recommender_system.ipynb
│── movies.pkl
│── similarity.pkl
│── requirements.txt
│── .gitignore
│── .gitattributes
│── csv files/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
```

---

## ⚙ How It Works

1. Data preprocessing and feature engineering in Jupyter Notebook.
2. Tags are created by combining:

   * Overview
   * Genres
   * Keywords
   * Cast
   * Crew
3. Text vectorization using CountVectorizer.
4. Similarity matrix generated using cosine similarity.
5. Saved into `.pkl` files for fast loading.
6. Streamlit frontend loads and displays recommendations.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yashgit-bit/movie-recommender-system.git
cd movie-recommender-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## 🔐 API Setup

This project uses OMDb API.

Create:

```bash
.streamlit/secrets.toml
```

Add:

```toml
OMDB_API_KEY = "your_api_key_here"
```

---

## 🌐 Deployment

Deployed using Streamlit Community Cloud.

---

## 📈 Future Improvements

* Better UI/UX (Netflix-style design)
* Search bar with autocomplete
* Genre filters
* Trending movies section
* Watchlist system
* User authentication
* Trailer integration
* Dark/light mode toggle

---

### 👨‍💻 Author

**Built by Yash Joshi**  
*Aspiring AI/ML Engineer*
