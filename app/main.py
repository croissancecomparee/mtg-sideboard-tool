from fastapi import FastAPI

app = FastAPI(title="MTG Sideboard Matrix Generator", description="API pour générer des matrices de sideboard pour Magic: The Gathering", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API MTG Sideboard Matrix Generator. Utilisez les endpoints pour générer des matrices de sideboard."}