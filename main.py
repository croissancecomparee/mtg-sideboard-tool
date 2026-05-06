import argparse
from src.parser import parse_decklist
from src.generator import generate_sideboard_matrix
from src.exporter import export_to_excel
from src.config_loader import load_formats_config

def list_formats():
    config = load_formats_config()
    print("📚 Formats disponibles :\n")
    for fmt, archetypes in config.items():
        print(f"🔹 {fmt}")
        for a in archetypes:
            print(f"   - {a}")
        print()

def main():
    try:
        parser = argparse.ArgumentParser(description="MTG Sideboard Matrix Generator")
        parser.add_argument("--format", type=str, required=True, help="Deck Format (e.g., Standard, Modern, Legacy)")
        parser.add_argument("--decklist", type=str, default="deck.txt", help="fichier decklist (format texte)")

        args = parser.parse_args()

        print(f"📦 Format choisi : {args.format}")
        print(f"📄 Deck input : {args.decklist}")

        decklist = parse_decklist(args.decklist)
        sideboard_matrix = generate_sideboard_matrix(decklist, args.format)
        export_to_excel(sideboard_matrix)
    except Exception as e:
        print(str(e))
        exit(1)

if __name__ == "__main__":
    main()