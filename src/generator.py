import pandas as pd
from src.config_loader import load_formats_config


def generate_sideboard_matrix(deck: dict, format_name: str) -> pd.DataFrame:
    '''
    fonction qui genere une matrice de sideboard a partir d'un decklist
    '''
    config = load_formats_config()
    format_name = format_name.lower()

    if format_name not in config:
        available = ", ".join(config.keys())
        raise ValueError(
            f"❌ Format inconnu: '{format_name}'\n"
            f"📚 Formats disponibles: {available}"
        )

    archetypes_by_format = config[format_name]

    if not archetypes_by_format:
        raise ValueError(f"Format '{format_name}' not found in configuration.")

    rows = []

    for card in deck.get("mainboard", []):
        row = {
            "Card": f"{card['quantity']} {card['name']}"
        }

        for archetype in archetypes_by_format:
            row[archetype] = ""
        
        rows.append(row)

    rows.append({"Card": "SIDEBOARD"})

    for card in deck.get("sideboard", []):
        row = {
            "Card": f"{card['quantity']} {card['name']}"
        }

        for archetype in archetypes_by_format:
            row[archetype] = ""
        
        rows.append(row)

    df = pd.DataFrame(rows)

    # ordre des colonnes
    cols = ["Card"] + archetypes_by_format
    df = df[cols]

    return df