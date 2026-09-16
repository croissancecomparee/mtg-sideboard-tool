from fastapi import FastAPI
from src.config_loader import load_formats_config

app = FastAPI(title="MTG Sideboard Matrix Generator", description="API pour générer des matrices de sideboard pour Magic: The Gathering", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API MTG Sideboard Matrix Generator. Utilisez les endpoints pour générer des matrices de sideboard."}

@app.get("/formats")
def get_formats():
    return load_formats_config()