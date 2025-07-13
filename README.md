# ShadowBreak_SQLite

Petit projet où je récupère les titres et liens d’articles depuis WeLoveBuzz, puis je les enregistre dans une base de données SQLite locale.

C’est une amélioration de la version précédente qui utilisait un fichier CSV. Ici, les données sont mieux structurées dans une vraie base `.db`, et les doublons sont automatiquement ignorés.

## Ce que ça fait

- Récupère les titres + liens d’articles depuis la page d’accueil
- Enregistre le tout dans une base de données SQLite (`articles.db`)
- Ignore les doublons grâce au champ `url` en unique
- Affiche combien d’articles ont été ajoutés

## Fichiers

- `scrape.py` → Script principal
- `requirements.txt` → Les bibliothèques utilisées
- `.gitignore` → Exclut le `.db` et le dossier `venv`
- `articles.db` → Généré automatiquement en lançant le script

## Comment lancer

```bash
pip install -r requirements.txt
python scrape.py
