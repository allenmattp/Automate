#! python3
# downloadXkcd.py - downloads every XKCD comic.

import requests, os, bs4, logging

# log any incidents where a comic can't be downloaded
logging.basicConfig(filename=os.path.join("xkcd", "missing_comics.txt"), level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


url = "https://xkcd.com"            # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd
while not url.endswith("#"):
    # Download the page
    print(f"Downloading page {url} ...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image
    comicElem = soup.select("#comic > img")
    if comicElem == []:
        print(f"Could not find comic image on page {url}.")
        logging.info(f"Could not find comic image on page {url}")
    else:
        comicUrl = "https:" + comicElem[0].get("src")

    # Download the image
    try:
        res = requests.get(comicUrl)
        res.raise_for_status()
        print(f"Downloading image {comicUrl}")
    except:
        # unrecognized URL
        print(f"Could not handle {comicUrl} on page {url}")
        logging.info(f"Could not handle {comicUrl} on page {url}")
        pass

    # Save the image to ./xkcd
    num = url.split("/")    # get comic number to prepend to path
    imageFile = open(os.path.join("xkcd", (num[-2] + "_" + os.path.basename(comicUrl))), "wb")
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    # Get the Prev button's url
    prevLink = soup.select("a[rel='prev']")[0]
    url = "https://xkcd.com" + prevLink.get("href")


print("Done.")