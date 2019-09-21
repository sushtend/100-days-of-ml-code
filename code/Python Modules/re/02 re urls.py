import re

urls = """
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

pattern = re.compile(r"https?://(www.)?(\w+)(\.\w+)")
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0))
    print(match.group(2))


pattern = re.compile(r"https?://(www.)?(\w+)(\.\w+)")
substituted_urls = pattern.sub(r"\2\3", urls)  # replaces entire url with group 2 & 3
print(substituted_urls)
