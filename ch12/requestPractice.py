import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()

print(len(res.text))
print(res.text[:100])

playFile = open("RomeAndJuliet.txt", "wb")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()