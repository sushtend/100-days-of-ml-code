from bs4 import BeautifulSoup
import requests
import csv

urls: dict = {}


def get_url(url):
    if url in urls:
        return urls[url]

    html = requests.get(url).text
    urls[url] = html
    return html


csv_file = open("we_scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline", "summary", "video"])

html = get_url("http://coreyms.com")
soup = BeautifulSoup(html, "lxml")

for article in soup.find_all("article"):
    try:

        headline = article.header.h2.a.text
        summary = article.find("div", class_="entry-content").p.text
        print(headline)
        print(summary)
        vid_src = article.find("iframe", class_="youtube-player")["src"]
        vid_src = vid_src.split("/")[4].split("?")[0]
        yt_link = f"https://www.youtube.com/watch?v={vid_src}"
    except Exception as e:
        yt_link = None
    print(yt_link)
    csv_writer.writerow([headline, summary, yt_link])
    print()

csv_file.close()
