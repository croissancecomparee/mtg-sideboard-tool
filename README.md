🧙‍♂️ Magic Sideboard Helper

Un outil Python pour automatiser la création de plans de sideboard pour les joueurs de Magic: The Gathering.

À partir d’une decklist texte (format Scryfall ou Moxfield), ce script génère un fichier CSV/Excel prérempli permettant de construire facilement des plans de sideboard par archétype.

🚀 Fonctionnalités (MVP)
📥 Parse une decklist .txt
🧱 Génère un tableau de sideboard prêt à remplir
🧠 Archétypes préconfigurés par format (Modern, Pioneer, etc.)
📊 Export en .csv ou .xlsx
⚡ CLI simple pour utilisation rapide
🖼️ Exemple
Input (decklist)
4 Lightning Bolt
2 Counterspell
1 Kaito Shizuki

Sideboard:
2 Stern Scolding
1 Toxic Deluge
Output (CSV / Excel)
Archetype	In	Out
Boros Energy		
Rakdos Scam		
Amulet Titan		
🛠️ Installation
git clone https://github.com/ton-username/magic-sideboard-helper.git
cd magic-sideboard-helper

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
▶️ Utilisation
python main.py --input deck.txt --format modern

Options :

--input : chemin vers la decklist
--format : format du deck (modern, pioneer, etc.)
--output : (optionnel) nom du fichier de sortie
📁 Structure du projet
project/
├── main.py
├── parser.py
├── generator.py
├── exporter.py
├── config/
│   └── formats.json
└── tests/
⚙️ Configuration

Les archétypes sont définis dans :

config/formats.json

Exemple :

{
  "modern": [
    "Boros Energy",
    "Rakdos Scam",
    "Amulet Titan"
  ]
}
🔮 Roadmap
 Export en texte lisible (matchup guide)
 Intégration Google Sheets
 API REST avec FastAPI
 Interface web simple
 Auto-complétion des cartes via Scryfall
🧪 Tests
pytest
💡 Objectif du projet

Ce projet a été conçu pour :

automatiser une tâche répétitive pour les joueurs de Magic
pratiquer le parsing, la manipulation de données et les exports
servir de projet de démonstration backend/data engineering
🤝 Contribution

Les contributions sont bienvenues !

Ajout de formats
Amélioration du parsing
Nouvelles fonctionnalités
📜 Licence

MIT

👤 Auteur

Ton Nom
[[LinkedIn](https://www.linkedin.com/in/ga%C3%A9tan-cece-440129215/)]
[[Portfolio](https://github.com/croissancecomparee)]