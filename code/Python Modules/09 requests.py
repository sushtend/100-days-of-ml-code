# http://httpbin.org
# https://www.youtube.com/watch?v=tb8gHvYlCFs&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=100

import requests

# r = requests.get("https://xkcd.com/353/")

# print(r)

# # print(dir(r))
# # print(help(r))

# print(r.content)

r = requests.get("https://imgs.xkcd.com/comics/python.png")

# with open("09 cominc.png", "wb") as f:
#     f.write(r.content)

print(r.status_code)
print(r.ok)
print(r.headers)

