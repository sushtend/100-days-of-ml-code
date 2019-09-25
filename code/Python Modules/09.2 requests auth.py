import requests


r = requests.get("https://httpbin.org/basic-auth/abdul/1234", auth=("abdulk", 1234))
print(r)


r = requests.get("https://httpbin.org/delay/6", timeout=3)  # Throws errror
print(r)

