from bs4 import BeautifulSoup
import requests
import csv


html = requests.get("https://economictimes.indiatimes.com").text

soup = BeautifulSoup(html, "lxml")

main_news = soup.find("div", class_="clearfix page-main-container").find(
    "div", class_="clearfix"
)

# article_url = main_news.hgroup.h1.find("a")["href"]
# article = main_news.hgroup.h1.a.text

# print(article_url)
# print(article)


ul = soup.find("ul", class_="mainrelatedstories")
# for li in ul.findAll("li"):
#     news = li.a.text
#     news_url = li.a["href"]
#     print(f" {news} : https://economictimes.indiatimes.com{news_url} ")
#     print()

# for h3 in main_news.findAll("h3"):
#     news = h3.a.text
#     news_url = h3.a["href"]
#     print(f" {news} : https://economictimes.indiatimes.com{news_url} ")
#     print()

widget_top_news = main_news.find("div", class_="tabsView newsTab").find(
    "div", class_="tabsContent"
)

for li in widget_top_news.ul.li.ul.findAll():

    try:
        news_url = li.find("a")["href"]
        news = li.a.text
        print(f" {news} : https://economictimes.indiatimes.com{news_url} ")
    except Exception as e:
        pass
    print()

