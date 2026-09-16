from fastapi import FastAPI
from pydantic import BaseModel

from src.config_loader import load_formats_config
from src.parser import parse_decklist_text
from src.generator import generate_sideboard_matrix

app = FastAPI(title="MTG Sideboard Matrix Generator", description="API pour générer des matrices de sideboard pour Magic: The Gathering", version="0.2.0",)

class GenerateRequest(BaseModel):
    decklist: str
    format: str

@app.get("/")
def home():
    return {"message": "Bienvenue sur l'API MTG Sideboard Matrix Generator. Utilisez les endpoints pour générer des matrices de sideboard."}

@app.get("/formats")
def get_formats():
    return load_formats_config()

@app.post("/generate")
def generate(request: GenerateRequest):
    deck = parse_decklist_text(request.decklist)

    matrix = generate_sideboard_matrix(deck, request.format)
    return matrix.fillna("").to_dict(orient="records")