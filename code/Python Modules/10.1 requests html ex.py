from requests_html import HTML, HTMLSession, AsyncHTMLSession
import csv


session = HTMLSession()
r = session.get("https://coreyms.com/")

for link in r.html.absolute_links:
    print(link)
