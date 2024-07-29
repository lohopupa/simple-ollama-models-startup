import requests
import time

default_models = ["llama3:8b", "qwen2:0.5b"]

url = "http://ollama:11434/api"

def list_models():
    query_url = url + "/tags"
    response = requests.get(query_url)
    return [m["name"] for m in response.json()["models"]]
    

def load_model(model_name):
    query_url = url + "/pull"
    response = requests.post(query_url, json={"name": model_name})
    if response.status_code == 200:
        print(f"Successfully loaded model: {model_name}")
    else:
        print(f"Failed to load model: {model_name}, Status Code: {response.status_code}, Response: {response.text}")

installed_models = list_models()
for model in default_models:
    if model in installed_models:
        print(f"Model {model} already installed!")
    else:
        load_model(model)