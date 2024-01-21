import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=87dea40effe476be98454b88c238f168&language=en-US"
    response = requests.get(url)
    data = response.json()
    return  'https://image.tmdb.org/t/p/w500'+ data['poster_path']


def recommend(movie):
    movie_index =  movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x:x[1])[1:6]
    recommended_movie = []
    recommended_movie_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_poster.append(fetch_poster(movie_id))

    return recommended_movie, recommended_movie_poster

movies = pd.DataFrame(pickle.load(open('movies.pkl', 'rb')))

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommendation System")

selected_movie_name = st.selectbox("Select Your Best Movie.", (movies['title'].values))
if st.button('Recommend'):
    mv_name, mv_poster = recommend(selected_movie_name)
    col1, col2,col3, col4, col5 = st.columns(5)
    with col1:
        st.text(mv_name[0])
        st.image(mv_poster[0])
    with col2:
        st.text(mv_name[1])
        st.image(mv_poster[1])
    with col3:
        st.text(mv_name[2])
        st.image(mv_poster[2])
    with col4:
        st.text(mv_name[3])
        st.image(mv_poster[3])
    with col5:
        st.text(mv_name[4])
        st.image(mv_poster[4])