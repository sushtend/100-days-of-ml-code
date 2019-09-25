# https://www.youtube.com/watch?v=a6fIbtFB46g&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=102
# https://pypi.org/project/requests-html/
from requests_html import HTML, HTMLSession
import csv


csv_file = open("web_scrapper.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Headline", "Summary", "URL"])

session = HTMLSession()
r = session.get("https://coreyms.com/")

articles = r.html.find("article")

# print(article.html)

for article in articles:
    headline = article.find(".entry-title-link", first=True).text
    print(headline)

    summary = article.find(".entry-content p", first=True).text
    print(summary)

    try:
        vid_src = article.find("iframe", first=True).attrs["src"]
        vid_id = vid_src.split("?")[0].split("/")[4]
        vid_url = f"https://www.youtube.com/watch?v={vid_id}"
    except Exception as e:
        vid_url = None
    print(vid_url)
    csv_writer.writerow([headline, summary, vid_url])
    print()
csv_file.close()
