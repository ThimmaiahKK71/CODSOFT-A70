import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

data = {
    'Title': [
        'Interstellar', 'The Shawshank Redemption', 'Finding Nemo', 'The Big Lebowski',
        'Gladiator', 'Forrest Gump', 'The Avengers', 'Inglourious Basterds'
    ],
    'Genre': [
        'Adventure Drama Sci-Fi', 'Drama', 'Animation Adventure Comedy', 'Comedy Crime',
        'Action Adventure Drama', 'Drama Romance', 'Action Adventure Sci-Fi', 'Adventure Drama War'
    ]
}

df = pd.DataFrame(data)

count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(df['Genre'])

cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

def recommend_movies(title, cosine_sim=cosine_sim):
    idx = df[df['Title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices]

print("Movies recommended for 'Interstellar':")
print(recommend_movies('Interstellar'))
