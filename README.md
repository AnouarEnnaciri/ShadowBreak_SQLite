# ShadowBreak_SQLite

A simple project where I scraped articles (titles and links) from WeLoveBuzz and saved them into a local SQLite database.

This version is an upgrade of the original CSV version — now using a proper table with duplicate checking and everything stored in a `.db` file.

## What It Does

- Scrapes article titles and URLs from the homepage
- Saves them into a `SQLite` database (`articles.db`)
- Skips duplicates using the `url` as a unique field
- Shows how many new articles were added

## Files

- `scrape.py` → The main script
- `requirements.txt` → Dependencies used
- `.gitignore` → Excludes `.db` and virtualenv
- `articles.db` → Auto-generated when you run the script

## How To Run

```bash
pip install -r requirements.txt
python scrape.py