# WebScraper – ShadowBreak

Un petit scraper Python qui récupère les titres et les liens d’articles depuis **WeLoveBuzz**, et les enregistre dans un fichier CSV.

## Fonctionnalités

- Contourne les protections simples anti-bot (via Chrome non-détecté)
- Récupère les titres + liens des articles récents
- Enregistre dans `samples/welovebuzz_articles.csv`
- Affiche un résumé propre dans le terminal

## Installation rapide

```bash
git clone https://github.com/ton_utilisateur/projectscrape3_shadowbreak.git
cd projectscrape3_shadowbreak
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
## Lancement
```bash
python scrape.py
