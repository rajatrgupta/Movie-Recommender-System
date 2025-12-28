import streamlit as st
import pickle
import pandas as pd
import requests

# =========================
#  OMDB POSTER FUNCTION
# =========================
OMDB_KEY = "7262e879"

def fetch_poster(movie_title):
    try:
        url = f"https://www.omdbapi.com/?t={movie_title}&apikey={OMDB_KEY}"
        data = requests.get(url).json()

        poster = data.get("Poster", None)
        if poster and poster != "N/A":
            return poster
        else:
            return "https://placehold.co/300x450?text=No+Image"

    except:
        return "https://placehold.co/300x450?text=No+Image"


# =========================
# LOAD DATA
# =========================
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies["title"].values

st.title("🎬 Movie Recommender System (OMDb Version)")

selected_movie = st.selectbox("Select a movie to get recommendations", movies_list)

def recommend(movie):
    index = movies[movies["title"] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_titles = []
    recommended_posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_titles.append(title)
        recommended_posters.append(fetch_poster(title))

    return recommended_titles, recommended_posters


if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])

