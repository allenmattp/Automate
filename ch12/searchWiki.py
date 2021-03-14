#! python3
# searchwiki.py - Searches wiki and either opens top 5 results or the returned wiki page

import requests, sys, webbrowser, bs4

print("Asking Wikipedia now ...")  # display text while downloading the search result page
res = requests.get('https://en.wikipedia.org/wiki/Special:Search?search=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result
linkElems = soup.select(".mw-search-result-heading > a")
if linkElems != []:
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        urlToOpen = "https://en.wikipedia.org/" + linkElems[i].get("href")
        print("Opening", urlToOpen)
        webbrowser.open(urlToOpen)
# Or go directly to the wikipedia page for entered search
else:
    urlToOpen = "https://en.wikipedia.org/wiki/" + ' '.join(sys.argv[1:])
    webbrowser.open(urlToOpen)