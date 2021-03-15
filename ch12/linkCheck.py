#! python3
# linkCheck.py - iterates through all links on a given website and prints the response

import requests, bs4

website = "https://automatetheboringstuff.com" # don't include the final "/"

print(f"Searching {website} for links now ...")
res = requests.get(website)
res.raise_for_status()

# Get website's html
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
linkElems = soup.findAll("a")   # search for all hyperlinks
if linkElems:   # if links are found
    for link in linkElems:  # iterate through all found links
        url = link.get("href")  # and grab the url
        if url and url[0] == "/":   # catch the relative links
            res = requests.get(website + url)
            print(f"Received {res.status_code} Status from {website + url}")
        elif url:   # if href found and not relative, assume absolute
            res = requests.get(url)
            print(f"Received {res.status_code} Status from {url}.")