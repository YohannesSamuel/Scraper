import animations
from bs4 import BeautifulSoup
import requests

RESET = "\033[0m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"

def formatter(res):
    animations.animatetext(f"\n{BLUE} [+] Searching for any onion links... {RESET}", 1.5)
    soup = BeautifulSoup(res, "html.parser")
    searchresults = soup.find_all("li", class_="result")
    results = ""
    for i in searchresults:
        soup2 = BeautifulSoup(str(i), "html.parser")
        description = str(soup2.find("p")).strip("<p></p>")
        title = str(soup2.find("a").encode_contents().decode()).strip("\n").strip('''                 
                  ''')
        url = str(soup2.find("cite")).strip("<cite></cite>")
        format = f'''
<li>
<h2>{title}</h2>
<p>{description}</p>
<a href="{url}">Visit Link</a>
</li>

'''
        results += format

    return results    


def request_sender(url):
    res = requests.get(url)
    return res.text


def main(keyword):
    url = f"https://ahmia.fi/search/?q={keyword}"
    response = request_sender(url)
    open("results.html", "w").write(response)
    results = formatter(response)
    return results

