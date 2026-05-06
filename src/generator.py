import pandas as pd


def generate_sideboard_matrix(deck: dict, format_name: str) -> pd.DataFrame:
    '''
    fonction qui genere une matrice de sideboard a partir d'un decklist
    '''
    # MVP : archétypes hardcodés (on fera config après)
    archetypes_by_format = {
        "modern": [
            "Boros Energy",
            "Rakdos Scam",
            "Amulet Titan",
            "Living End",
            "Hammer Time"
        ],
        "legacy": [
            "Delver",
            "Reanimator",
            "Storm",
            "Death & Taxes"
        ]
    }

    archetypes = archetypes_by_format.get(format_name.lower(), [])

    rows = []

    for card in deck.get("mainboard", []):
        row = {
            "Card": f"{card['quantity']} {card['name']}"
        }

        for archetype in archetypes:
            row[archetype] = ""
        
        rows.append(row)

    rows.append({"Card": "SIDEBOARD"})

    for card in deck.get("sideboard", []):
        row = {
            "Card": f"{card['quantity']} {card['name']}"
        }

        for archetype in archetypes:
            row[archetype] = ""
        
        rows.append(row)

    df = pd.DataFrame(rows)

    # ordre des colonnes
    cols = ["Card"] + archetypes
    df = df[cols]

    return df