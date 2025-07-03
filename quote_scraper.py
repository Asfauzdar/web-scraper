import time
import requests
from bs4 import BeautifulSoup

print("🎯 WELCOME TO THE WEB SCRAPER")
time.sleep(1)
print("📚 THIS IS A QUOTES SCRAPER")
time.sleep(1)

# User inputs
url = input("🔗 Enter the website URL (e.g., http://quotes.toscrape.com): ").strip()
author_input = input("👤 Enter author name to filter (e.g., Albert Einstein): ").strip().lower()
page = 1
all_quotes = []
found = False  # To track if matching quote was found

while True:
    try:
        # Send request to the website(opening)
    
        response = requests.get(f"{url}/page/{page}/")
        response.raise_for_status()  # Raises error if not 200 OK
    except requests.exceptions.RequestException as e:
        
        print("\n❌ Could not access the site.")
        print("Details:", e)
        break
 

     # Parse(breaking into components) the website

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.find_all("div", class_="quote")

    if not quotes:
        break  # No more quotes/pages


    for quote in quotes:
        try:
            text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text

            # Check for match
            if author.lower() == author_input:
                found = True
                print("\n📝 Quote:", text)
                print("👤 Author:", author)
                print("--------")
                all_quotes.append(f"{text} - {author}\n")

        except AttributeError:
            print("⚠️ Skipped one quote due to missing data.")
            continue

    page+=1 #for moving to next page

if found:
    f=open("quotes.txt", "w" , encoding="utf-8")
    f.writelines(all_quotes)
    print("\n✅ Quotes saved to 'quotes.txt'")
else:
    print(f"\n⚠️ No quotes found for: {author_input}")

