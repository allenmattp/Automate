import bs4, requests

def getQuote(ticker):
    site = "https://finance.yahoo.com/quote/" + ticker
    res = requests.get(site)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    last_price = soup.select("#quote-header-info > div.My\(6px\).Pos\(r\).smartphone_Mt\(6px\) > div.D\(ib\).Va\(m\).Maw\(65\%\).Ov\(h\) > div > span.Trsdu\(0\.3s\).Fw\(b\).Fz\(36px\).Mb\(-4px\).D\(ib\)")
    bid = soup.select("#quote-summary > div.D\(ib\).W\(1\/2\).Bxz\(bb\).Pend\(12px\).Va\(t\).ie-7_D\(i\).smartphone_D\(b\).smartphone_W\(100\%\).smartphone_Pend\(0px\).smartphone_BdY.smartphone_Bdc\(\$seperatorColor\) > table > tbody > tr:nth-child(3) > td.Ta\(end\).Fw\(600\).Lh\(14px\) > span")
    ask = soup.select("#quote-summary > div.D\(ib\).W\(1\/2\).Bxz\(bb\).Pend\(12px\).Va\(t\).ie-7_D\(i\).smartphone_D\(b\).smartphone_W\(100\%\).smartphone_Pend\(0px\).smartphone_BdY.smartphone_Bdc\(\$seperatorColor\) > table > tbody > tr:nth-child(4) > td.Ta\(end\).Fw\(600\).Lh\(14px\) > span")
    cap = soup.select("#quote-summary > div.D\(ib\).W\(1\/2\).Bxz\(bb\).Pstart\(12px\).Va\(t\).ie-7_D\(i\).ie-7_Pos\(a\).smartphone_D\(b\).smartphone_W\(100\%\).smartphone_Pstart\(0px\).smartphone_BdB.smartphone_Bdc\(\$seperatorColor\) > table > tbody > tr:nth-child(1) > td.Ta\(end\).Fw\(600\).Lh\(14px\) > span")
    try:
        print(f"{ticker.upper()}:\nLast price: ${last_price[0].text.strip()}\n"
              f"Bid: ${bid[0].text.strip()}\n"
              f"Ask: ${ask[0].text.strip()}\n"
              f"Market Cap: ${cap[0].text.strip()}")
    except IndexError:
        print(f"Issue with {ticker}... Skipping")

def getSymbols(file):
    with open(file, "r") as f:
        line = f.readline()
        ticker_list = []
        while line:
            ticker_list.append(line.split())
            line = f.readline()
    f.close()

    return ticker_list

if __name__ == '__main__':
    ticker_list = getSymbols("symbols.txt")
    for ticker in ticker_list:
        getQuote(ticker[0])
        print() # line break