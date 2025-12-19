import requests
import pytest

URL = "https://jsonplaceholder.typicode.com"


# Escenario 1: UPDATE (PUT) - Modificar algo que ya existe
def test_actualizar_post():
    # Vamos a modificar el Post #1
    endpoint = f"{URL}/posts/1"

    payload_nuevo = {
        "id": 1,
        "title": "Título Actualizado por Pytest",
        "body": "Este cuerpo fue reemplazado usando el método PUT.",
        "userId": 1
    }

    response = requests.put(endpoint, json=payload_nuevo)

    # Validaciones
    assert response.status_code == 200, f"Fallo al actualizar. Status: {response.status_code}"
    data = response.json()
    assert data["title"] == "Título Actualizado por Pytest", "El título no cambió"
    print("\n✅ Update (PUT) funcionó correctamente.")


# Escenario 2: DELETE - Borrar un recurso
def test_borrar_post():
    endpoint = f"{URL}/posts/1"

    response = requests.delete(endpoint)

    # JSONPlaceholder devuelve 200 cuando borras (otros APIs devuelven 204)
    assert response.status_code == 200, f"Fallo al borrar. Status: {response.status_code}"
    # Validamos que devuelva un JSON vacío {} (señal de que se fue)
    assert response.json() == {}, "El cuerpo de respuesta debería estar vacío"
    print("\n✅ Delete (DELETE) funcionó correctamente.")


# Escenario 3: QUERY PARAMS - Filtrar información
def test_filtrar_comentarios():
    # Queremos solo los comentarios del Post #1
    # URL real: https://jsonplaceholder.typicode.com/comments?postId=1
    endpoint = f"{URL}/comments"
    parametros = {"postId": 1}

    response = requests.get(endpoint, params=parametros)

    assert response.status_code == 200
    data = response.json()

    # Validamos que trajimos una lista y que tiene elementos
    assert len(data) > 0, "No se encontraron comentarios"

    # Validamos que el primer comentario sea realmente del postId 1
    assert data[0]["postId"] == 1, "El filtro falló, trajo comentarios de otro post"
    print(f"\n✅ Filtro funcionó. Se encontraron {len(data)} comentarios del Post 1.")


# Escenario 4: NEGATIVE TEST - Buscar algo que no existe
def test_recurso_no_encontrado():
    # El post 9999 no existe
    endpoint = f"{URL}/posts/9999"

    response = requests.get(endpoint)

    # AQUÍ ESPERAMOS UN ERROR (404). Si da 200, el test falla.
    assert response.status_code == 404, f"Esperaba un 404, pero llegó {response.status_code}"
    print("\n✅ Test Negativo funcionó: La API devolvió 404 correctamente.")
