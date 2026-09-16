# 🧙‍♂️ Magic Sideboard Helper

Un outil Python pour automatiser la création de plans de sideboard pour les joueurs de Magic: The Gathering.

À partir d’une decklist texte (format Scryfall ou Moxfield), ce script génère un fichier CSV/Excel prérempli permettant de construire facilement des plans de sideboard par archétype.

### Mvp 2:
en plus, avoir un support utilisable par d'autres utilisateurs sans utiliser des lignes de commandes soit via api, appli web ou exécutable (à voir ?)

## 🚀 Fonctionnalités (MVP)
📥 Parse une decklist .txt
🧱 Génère un tableau de sideboard prêt à remplir
🧠 Archétypes préconfigurés par format (Modern, Pioneer, etc.)
📊 Export en .csv ou .xlsx
⚡ CLI simple pour utilisation rapide
📊 Ajout d'une interface web

## 🔮 Roadmap

### MVP 1 — CLI tool ✅

- [x] Parse text decklists
- [x] Load archetypes from configuration
- [x] Generate sideboard planning matrix
- [x] Export Excel
- [x] Export text sideboard guide
- [x] CLI format selection
- [x] CLI validation

### MVP 2 — Web application 🚧

- [ ] Refactor the core into a reusable Python module
- [ ] Add FastAPI backend
- [ ] Add HTML interface
- [ ] Allow users to paste decklists
- [ ] Select a Magic format from the interface
- [ ] Generate sideboard plans from the browser
- [ ] Download Excel files
- [ ] Download text sideboard guides

### Future

- [ ] Editable sideboard matrix in the browser
- [ ] Scryfall API integration
- [ ] Card name validation and auto-completion
- [ ] Google Sheets integration
- [ ] Save sideboard plans
- [ ] User accounts

## 🖼️ Exemple
Input (decklist)
4 Lightning Bolt
2 Counterspell
1 Kaito Shizuki

## Sideboard:
2 Stern Scolding
1 Toxic Deluge
Output (CSV / Excel)
Archetype	In	Out
Boros Energy		
Rakdos Scam		
Amulet Titan		
## 🛠️ Installation
git clone https://github.com/ton-username/magic-sideboard-helper.git
cd magic-sideboard-helper

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

pip install -r requirements.txt
## ▶️ Utilisation
python main.py --input deck.txt --format modern

Options :

--input : chemin vers la decklist
--format : format du deck (modern, pioneer, etc.)
--output : (optionnel) nom du fichier de sortie

## 📁 Structure du projet
project/
├── app/                    # Web application
│   ├── main.py             # FastAPI application
│   ├── templates/          # HTML templates
│   └── static/             # CSS / JavaScript
│
├── src/                    # Core application logic
│   ├── parser.py
│   ├── generator.py
│   ├── exporter.py
│   ├── text_exporter.py
│   └── config_loader.py
│
├── main.py
├── parser.py
├── generator.py
├── exporter.py
├── config/
│   └── formats.json
└── tests/
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore

## ⚙️ Configuration

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
## 🔮 Roadmap
 Export en texte lisible (matchup guide)
 Intégration Google Sheets
 API REST avec FastAPI
 Interface web simple
 Auto-complétion des cartes via Scryfall
## 🧪 Tests
pytest
## 💡 Objectif du projet

Ce projet a été conçu pour :

automatiser une tâche répétitive pour les joueurs de Magic
pratiquer le parsing, la manipulation de données et les exports
servir de projet de démonstration backend/data engineering
## 🤝 Contribution

Les contributions sont bienvenues !

Ajout de formats
Amélioration du parsing
Nouvelles fonctionnalités
## 📜 Licence

MIT

## 👤 Auteur

Gaétan Cece
[[LinkedIn](https://www.linkedin.com/in/ga%C3%A9tan-cece-440129215/)]
[[Portfolio](https://github.com/croissancecomparee)]
