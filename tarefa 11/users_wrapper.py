import requests
 
API_URL = "https://jsonplaceholder.typicode.com"
 
def list():
    response = requests.get(f"{API_URL}/users")
    return response.json() if response.status_code == 200 else False
 
def create(dados):
    response = requests.post(f"{API_URL}/users", json=dados)
    return response.json() if response.status_code == 201 else False
 
def read(user_id):
    response = requests.get(f"{API_URL}/users/{user_id}")
    return response.json() if response.status_code == 200 else False
 
def update(user_id, dados):
    response = requests.put(f"{API_URL}/users/{user_id}", json=dados)
    return response.json() if response.status_code == 200 else False
 
def delete(user_id):
    response = requests.delete(f"{API_URL}/users/{user_id}")
    return response.status_code == 200