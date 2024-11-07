import random
import urllib.request
import webbrowser
import urllib.parse

# URL for the movie list
movie_list_url = "https://gist.githubusercontent.com/n8foo/6c4e2a492c8479648d1e/raw/c13157e1fb6e9db92e0253023a10effc802f6ea4/allmovies.txt"

# Define keywords associated with each mood
mood_keywords = {
    "happy": ["happy", "joy", "sunshine", "adventure", "smile", "wonderful"],
    "sad": ["tears", "heartbreak", "loss", "grief", "goodbye", "sorrow"],
    "action": ["war", "fight", "battle", "mission", "hero", "danger"],
    "romantic": ["love", "heart", "romance", "kiss", "wedding", "affair"],
    "comedy": ["comedy", "funny", "laugh", "silly", "crazy", "party"],
    "horror": ["horror", "nightmare", "fear", "death", "scary", "haunt"]
}

# Fetch and split the movie list into lines
def fetch_movie_list():
    response = urllib.request.urlopen(movie_list_url)
    data = response.read().decode("utf-8")
    movie_list = data.splitlines()
    return movie_list

# Select movies based on mood keywords
def filter_movies_by_mood(mood, movie_list):
    keywords = mood_keywords.get(mood, [])
    filtered_movies = [movie for movie in movie_list if any(keyword.lower() in movie.lower() for keyword in keywords)]
    
    # If no movies matched, return a random selection as a fallback
    if not filtered_movies:
        print(f"No specific matches found for mood '{mood}'. Selecting a random movie instead.")
        return random.choice(movie_list)
    
    return random.choice(filtered_movies)

# Generate a Plex search URL
def generate_plex_search_url(movie_title):
    encoded_title = urllib.parse.quote(movie_title)
    search_url = f"https://app.plex.tv/#!/search?pivot=top&query={encoded_title}"
    return search_url

# Main player function
def plex_mood_player():
    movie_list = fetch_movie_list()
    mood = input("How are you feeling today? (happy, sad, action, romantic, comedy, horror): ").lower()
    
    # Get a movie based on the mood
    movie = filter_movies_by_mood(mood, movie_list)
    print(f"Based on your mood, we recommend: {movie}")
    
    # Open movie in Plex
    plex_url = generate_plex_search_url(movie)
    webbrowser.open(plex_url)
    print(f"Opening movie URL: {plex_url}")

# Example usage
plex_mood_player()
