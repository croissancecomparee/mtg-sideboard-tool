import pandas as pd


def generate_sideboard_table(deck: dict, format_name: str) -> pd.DataFrame:
    '''
    fonction qui genere une table de sideboard a partir d'un decklist
    '''
    sideboard = deck.get("sideboard", [])
    data = []
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

    data = []

    for archetype in archetypes:
        data.append({
            "Archetype": archetype,
            "In": "",
            "Out": ""
        })

    df = pd.DataFrame(data)

    return df