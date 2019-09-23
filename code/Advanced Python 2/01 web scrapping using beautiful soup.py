# https://www.youtube.com/watch?v=ng2o98k983k

from bs4 import BeautifulSoup
import requests

with open("Advanced Python 2/01.1 simple.html", "r") as html_file:
    soup = BeautifulSoup(html_file, "lxml")

# print(soup.prettify())


match = soup.title.text
print(match)

# match = soup.div

# # Note thet class_ because class is a keyword in python
# article = soup.find("div", class_="article")
# print(article)

# headline = article.h2.a.text
# summary = article.p.text
# print("Headline is : --> ", headline)
# print("Summary  is : --> ", summary)


for article in soup.find_all("div", class_="article"):
    headline = article.h2.a.text
    summary = article.p.text
    print("Headline is : --> ", headline)
    print("Summary  is : --> ", summary)
    print()

