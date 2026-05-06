import re

def parse_decklist(file_path: str) -> dict:
    '''
    fonction qui recupere les cartes d'un decklist et les organise dans un dictionnaire
    '''
    mainboard = []
    sideboard = []

    current_section = 'mainboard'

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # ignore empty lines
            if not line:
                continue

            # detect sideboard or mainboard section
            if re.match(r'^(sideboard|mainboard)$', line, re.IGNORECASE):
                current_section = line.lower()
                continue

            match = re.match(r"(\d+)\s+(.+)", line)

            if not match:
                print(f"Warning: line '{line}' does not match expected format and will be skipped.")
                continue

            qty = int(match.group(1))
            name = match.group(2).strip()

            card = {
                "name": name,
                "quantity": qty
            }

            if current_section == 'mainboard':
                mainboard.append(card)
            else:
                sideboard.append(card)

    return {
        "mainboard": mainboard,
        "sideboard": sideboard
    }