import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# use the requests module to get the HTML of the website’s main page
main_url = "http://books.toscrape.com/index.html"
result = requests.get(main_url) 
soup = BeautifulSoup(result.text, 'html.parser')
# define a function to request and parse a HTML web page
def getAndParseURL(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return(soup)
main_page_products_urls = [products.div.a.get('href') for products in soup.findAll("article", class_ = "product_pod")]
# define a function to retrieve book links on any given page of the website
def getBooksURLs(url):
    soup = getAndParseURL(url)
    # remove the index.html part of the base url before returning the results
    return(["/".join(url.split("/")[:-1]) + "/" + x.div.a.get('href') for x in soup.findAll("article", class_ = "product_pod")])
pages_urls = []
new_page = "http://books.toscrape.com/catalogue/page-1.html"
while requests.get(new_page).status_code == 200:
    pages_urls.append(new_page)
    new_page = pages_urls[-1].split("-")[0] + "-" + str(int(pages_urls[-1].split("-")[1].split(".")[0]) + 1) + ".html"

booksURLs = []
for page in pages_urls:
    booksURLs.extend(getBooksURLs(page))
# get product data
names = []
prices = []
categories = []
ratings = []
# scrape data for every book URL: this may take some time
for url in booksURLs:
    soup = getAndParseURL(url)
    # product name
    names.append(soup.find("div", class_ = re.compile("product_main")).h1.text)
    # product price
    prices.append(soup.find("p", class_ = "price_color").text[2:]) # get rid of the pound sign          
    # product category
    categories.append(soup.find("a", href = re.compile("../category/books/")).get("href").split("/")[3])
    # ratings
    ratings.append(soup.find("p", class_ = re.compile("star-rating")).get("class")[1])

#add data into pandas df
scraped_data = pd.DataFrame({'name': names, 'price': prices, "product_category": categories, "rating": ratings})
scraped_data.to_csv('books.csv', index=False, encoding='utf-8')
