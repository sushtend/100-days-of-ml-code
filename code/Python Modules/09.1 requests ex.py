import requests


payload = {"page": 2, "count": 25}
r = requests.get("https://httpbin.org/get", params=payload)
print(r.text)

print(r.url)


print("POST request")

payload = {"uname": "abdul", "pwd": "1234"}
r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
print(r.json())

r_dict = r.json()

print(r_dict["form"])

