# Scraped all items from https://www.microfocus.com/en-us/products?trial=true through DevTools into website.html. For a dynamic retrieval solution Selenium/requests can be leveraged.
# Resulting JSON file: https://github.com/a4ojha/open-text-application/test2/products.json

# Each product will have the following items:
    # Product Name
    # Starting Letter, ex. "Adoption Readiness Tool" à "A"
    # Description
    # Free Trial / Demo Request URL
    # Support Link URL
    # Community Link URL

from bs4 import BeautifulSoup
import json

# Read website content
with open('website.html', 'r', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

product_grid = soup.find_all(class_='products-grid')[0]
products = []
count = 0

base_url = "https://www.microfocus.com"
def build_url(path):
    if path[0] == "/":
        return base_url + path
    return path

# iterate through letter blocks (A, B, C...)
for letter_block in product_grid.find_all(class_="letter-block"):
    # Grab the letter
    letter = letter_block.find_all(class_="each-letter-scroll")[0].find_all('span')[0].text
    
    # Loop through items in the letter block
    for card in letter_block.find_all(class_="uk-card"):
        products.append({'Starting Letter': letter})
        
        # Product name
        products[count]['Product Name'] = card.find_all('h3')[0].find_all(class_="block-header")[0].text  
        
        # Description
        products[count]["Description"] = card.find_all(class_="description")[0].find_all('p')[0].text
        
        # Trial / demo URL(s)
        cta = card.find_all(class_="cta-buttons")[0]
        for url in cta:
            if url.text == "Get free trial":
                products[count]["Free Trial URL"] = build_url(url.get('href'))
            if url.text == "Request a demo":
                products[count]["Demo URL"] = build_url(url.get('href'))
        
        # Support / community URLs
        footer = card.find_all(class_="footer")
        for url in footer[0].find_all('a'):
            if len(url.text) > 0:
                if url.text == "Community":
                    products[count]["Community URL"] = build_url(str(url.get('href')))
                if url.text == "Support":
                    products[count]["Support URL"] = build_url(str(url.get('href')))                
        
        count += 1
        
# Write JSON object to file
with open("products.json", "w", encoding="utf-8") as json_file:
        json.dump(products, json_file, indent=4, ensure_ascii=False)
