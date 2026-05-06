from src.parser import parse_decklist
from src.generator import generate_sideboard_table
from src.exporter import export_to_excel

if __name__ == "__main__":
    decklist = parse_decklist("deck.txt")
    print(decklist)
    sideboard_table = generate_sideboard_table(decklist, "modern")
    export_to_excel(sideboard_table)
    # print("MAINBOARD")
    # for card in decklist["mainboard"]:
    #     print(f"{card['quantity']} {card['name']}")
    #     # print()

    # print("\nSIDEBARD")
    # for card in decklist["sideboard"]:
    #     print(f"{card['quantity']} {card['name']}")