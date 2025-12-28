# 🎬 Movie Recommender System

A content-based movie recommendation system built with Streamlit that suggests similar movies based on user selection. The app fetches movie posters from the OMDb API to provide a visual experience.

## Features

- 🎯 Content-based movie recommendations
- 🖼️ Movie poster display using OMDb API
- 🎨 Clean and intuitive Streamlit interface
- 📊 Based on movie similarity matrix

## Requirements

- Python 3.7+
- Streamlit
- Pandas
- Requests
- Pickle files: `movie_list.pkl` and `similarity.pkl`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/rajatrgupta/Movie-Recommender-System.git
cd Movie-Recommender-System
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure you have the required pickle files (`movie_list.pkl` and `similarity.pkl`) in the `models/` directory.

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Select a movie from the dropdown menu and click "Recommend" to get 5 similar movie recommendations with posters.

## Project Structure

```
Movie Recommender System/
├── app.py                              # Main Streamlit application
├── Movie Recommender System.ipynb      # Jupyter notebook for data processing
├── requirements.txt                    # Python dependencies
├── README.md                          # Project documentation
├── .gitignore                         # Git ignore file
├── data/                               # Data directory
│   ├── tmdb_5000_movies.csv           # Movies dataset
│   └── tmdb_5000_credits.csv          # Credits dataset
└── models/                             # Models directory
    ├── movie_list.pkl                  # Processed movie dataset
    ├── similarity.pkl                  # Similarity matrix
    ├── movie_dict.pkl                  # Movie dictionary
    └── posters.pkl                     # Movie posters data
```

## API Key

The app uses the OMDb API to fetch movie posters. The API key is currently hardcoded in `app.py`. For production use, consider using environment variables or Streamlit secrets.

## License

This project is open source and available for personal use.

