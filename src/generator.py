import pandas as pd
from src.config_loader import load_formats_config


def generate_sideboard_matrix(deck: dict, format_name: str) -> pd.DataFrame:
    '''
    fonction qui genere une matrice de sideboard a partir d'un decklist
    '''

    archetypes_by_format = load_formats_config().get(format_name.lower(), [])

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