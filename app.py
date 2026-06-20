import streamlit as st
import pickle
import requests

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))


# Convert runtime into hours and minutes
def convert_runtime(runtime):
    if runtime == "N/A":
        return "Unknown"

    minutes = int(runtime.split()[0])
    hours = minutes // 60
    mins = minutes % 60

    return f"{hours}h {mins}m"


# Fetch movie details from OMDb API
def fetch_movie_details(movie_name):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={st.secrets['OMDB_API_KEY']}"
    data = requests.get(url).json()

    return {
        'poster': data['Poster'] if data.get('Poster') != 'N/A' else 'https://via.placeholder.com/300x450?text=No+Poster',
        'year': data.get('Year', 'N/A'),
        'rating': data.get('imdbRating', 'N/A'),
        'genre': data.get('Genre', 'N/A'),
        'runtime': convert_runtime(data.get('Runtime', 'N/A')),
        'plot': data.get('Plot', 'No plot available')
    }


# Recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_data = []

    for i in movies_list:
        movie_title = movies.iloc[i[0]].title
        recommended_movies.append(movie_title)
        recommended_movies_data.append(fetch_movie_details(movie_title))

    return recommended_movies, recommended_movies_data


# Session state for recommendation chain
if 'selected_movie' not in st.session_state:
    st.session_state.selected_movie = movies['title'].values[0]


st.title("🎬 Movie Recommender System")
st.markdown("### Discover movies similar to your favorites")
st.divider()


# Movie selection dropdown
selected_movie_name = st.selectbox(
    '🔍 Search or select a movie',
    movies['title'].values,
    index=list(movies['title'].values).index(st.session_state.selected_movie)
)

# Update selected movie
st.session_state.selected_movie = selected_movie_name

# Fetch selected movie details
selected_movie_data = fetch_movie_details(selected_movie_name)

# Selected movie section
st.subheader("🎥 Selected Movie")
st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.image(selected_movie_data['poster'], use_container_width=True)

with col2:
    st.markdown(f"### {selected_movie_name}")
    st.markdown(
        f"""
    ⭐ **{selected_movie_data['rating']}**  
    📅 {selected_movie_data['year']}  
    🎭 {selected_movie_data['genre']}  
    ⏱ {selected_movie_data['runtime']}  

    📝 **Plot:**  
    {selected_movie_data['plot']}
    """
    )


#recommendations
with st.spinner("Finding similar movies..."):
    recommendations, movies_data = recommend(selected_movie_name)

st.subheader("🍿 Recommended Movies")
st.divider()

cols = st.columns(5)

for i in range(5):
    with cols[i]:
        st.image(movies_data[i]['poster'], use_container_width=True)

        # Make title the clickable selector
        if st.button(recommendations[i], key=f"movie_{i}"):
            st.session_state.selected_movie = recommendations[i]
            st.rerun()

        st.markdown(
            f"""
        ⭐ **{movies_data[i]['rating']}**  
        📅 {movies_data[i]['year']}  
        🎭 {movies_data[i]['genre']}  
        ⏱ {movies_data[i]['runtime']}
        """
        )