import bs4, requests

def getPrice(site):
    res = requests.get(site)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    name_raw = soup.select("#itemTitle")
    name = name_raw[0].text.strip()
    price = soup.select("#prcIsum")
    print(f"{name[16:]} is currently {price[0].text.strip()}")

wishlist = [
    "https://www.ebay.com/itm/Warhammer-Underworlds-Direchasm/133602916208",
    "https://www.ebay.com/itm/Dominion-of-Sigmar-Penumbral-Stormvault-Terrain-Warhammer-AoS-Games-Workshop/184019528671",
    "https://www.ebay.com/itm/Games-Workshop-Warhammer-Age-of-Sigmar-Shadow-and-Pain-Box-Set/363177183255"
]

if __name__ == '__main__':
    for item in wishlist:
        getPrice(item)
        print()