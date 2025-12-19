import requests
import pytest

URL = "https://jsonplaceholder.typicode.com"
HEADERS = {

"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

}
def test_api():
    endpoint = f"{URL}/posts"
    response = requests.get(endpoint, headers=HEADERS)
    assert response.status_code == 200, f"Error: No se pudo entrar a la API"
    posters = {
        "title": "Titulo",
        "body": "Cuerpo",
        "userId": 100
    }

    response = requests.post(endpoint, json=posters, headers=HEADERS)
    assert response.status_code == 201, f"Error: No se pudo publicar el poster. {response.status_code}"
