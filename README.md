# Web Scraper: Quotes by Author (Python)

This is a simple Python script that scrapes quotes from [http://quotes.toscrape.com](http://quotes.toscrape.com) and filters them by a given author's name. It automatically loops through all pages and saves matching quotes to a `.txt` file.

---

## 🚀 Features

* Takes input from user for author name
* Scrapes quotes from **all pages**
* Filters quotes by author (case-insensitive, punctuation-tolerant)
* Saves matching quotes to `quotes.txt`
* Handles broken quotes or network issues gracefully

---

## 💻 How to Run

```bash
python quote_scraper.py
```

Then input:

* Website URL (e.g. `http://quotes.toscrape.com`)
* Author name (e.g. `albert einstein`)

---

## 📝 Example Output

```
📝 Quote: “Logic will get you from A to Z; imagination will get you everywhere.”
👤 Author: Albert Einstein
--------
```

Saved to `quotes.txt`

---

## 🌟 Credits

Built by Abhimanyu Singh Fauzdar 
