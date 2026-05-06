import argparse
from src.parser import parse_decklist
from src.generator import generate_sideboard_matrix
from src.exporter import export_to_excel

def main():
    parser = argparse.ArgumentParser(description="MTG Sideboard Matrix Generator")
    parser.add_argument("--format", type=str, required=True, help="Deck Format (e.g., Standard, Modern, Legacy)")
    parser.add_argument("--decklist", type=str, default="deck.txt", help="fichier decklist (format texte)")

    args = parser.parse_args()

    print(f"📦 Format choisi : {args.format}")
    print(f"📄 Deck input : {args.decklist}")

    decklist = parse_decklist(args.decklist)
    sideboard_matrix = generate_sideboard_matrix(decklist, args.format)
    export_to_excel(sideboard_matrix)

if __name__ == "__main__":
    main()