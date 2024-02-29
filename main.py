import requests

def search_movie_by_title(title):
    api_key "Sua API KEY aqui" 
    base_url = "https://api.themoviedb.org/3/search/movie"
    
    params = {
        "api_key": api_key,
        "query": title
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "results" in data and data["results"]:
        movie = data["results"][0]
        print(f"Filme Encontrado: {movie['title']} ({movie['release_date'][:4]})")
        print(f"Sinopse: {movie['overview']}")
    else:
        print("Nenhum filme encontrado.")

# loop para enquanto não escrever exit continuar perguntando
if __name__ == "__main__":
    while True:
        movie_title = input("Digite o título do filme (ou 'exit' para sair): ")
        if movie_title.lower() == 'exit':
            break
        search_movie_by_title(movie_title)
