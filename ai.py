import requests

def ask(question): 
    response = requests.post("http://localhost:8080/completion", json={
        "prompt": question,
        "n_predict": 64
    })
    return response.json()["content"]