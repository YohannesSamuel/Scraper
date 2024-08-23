import os
import animations
import reportgenerator
import requests
from bs4 import BeautifulSoup

RESET = "\033[0m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
WHITE = "\033[0;37m"
BOLD_BLACK = "\033[1;30m"
BOLD_RED = "\033[1;31m"
BOLD_GREEN = "\033[1;32m"
BOLD_YELLOW = "\033[1;33m"
BOLD_BLUE = "\033[1;34m"
BOLD_PURPLE = "\033[1;35m"
BOLD_CYAN = "\033[1;36m"
BOLD_WHITE = "\033[1;37m"
UNDERLINE_BLACK = "\033[4;30m"
UNDERLINE_RED = "\033[4;31m"
UNDERLINE_GREEN = "\033[4;32m"
UNDERLINE_YELLOW = "\033[4;33m"
UNDERLINE_BLUE = "\033[4;34m"
UNDERLINE_PURPLE = "\033[4;35m"
UNDERLINE_CYAN = "\033[4;36m"
UNDERLINE_WHITE = "\033[4;37m"
BACKGROUND_BLACK = "\033[40m"
BACKGROUND_RED = "\033[41m"
BACKGROUND_GREEN = "\033[42m"
BACKGROUND_YELLOW = "\033[43m"
BACKGROUND_BLUE = "\033[44m"
BACKGROUND_PURPLE = "\033[45m"
BACKGROUND_CYAN = "\033[46m"
BACKGROUND_WHITE = "\033[47m"

os.popen("rm results.html")

links = [
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "youtube.com",
    "tiktok.com",
]


methods = [
    "",
    "intitle:",
    "inurl:",
    "intext:"
]

def request_sender(query):
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.447"
    r = requests.get(f"https://google.com/search?q={query}")
    return r.text


facebookresults = ""
twitterresults = ""
instagramresults = ""
linkedinresults = ""
youtuberesults = ""
tiktokresults = ""

def formatter(res):
    open("requestresult.html", "ab").write(str(res).encode())
    soup1 = BeautifulSoup(res, "html.parser")
    results = soup1.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")
    for i in results:
        try:
            soup2 = BeautifulSoup(str(i), "html.parser")
            link = str(soup2.find("a")["href"])[7:]
            title = str(soup2.find("div", class_="BNeawe vvjwJb AP7Wnd")).strip('<div class="BNeawe vvjwJb AP7Wnd">').strip('</div>')
            description = soup2.find("div", class_="BNeawe s3v9rd AP7Wnd")
            if description:
                description = str(description).strip('<div class="BNeawe s3v9rd AP7Wnd"><div><div><div class="BNeawe s3v9rd AP7Wnd">').strip('</div></div></div></div>').strip('<div class="BNeawe vvjwJb AP7Wnd">').strip('</div>')
            form1 = f'''
    {link}
    {title}
    {description}
    '''
            htmlformat = f'''
<li>
<h2>{title}</h2>
<p>{description}</p>
<a href="{link}" target="_blank">Visit site</a>
</li>



'''
            if "<" not in link and "<" not in description and "<" not in title:
                open("results.html", "a").write(str(htmlformat))
                # print(htmlformat)
            else:
                continue
        except:
            continue    



def main(name):
    facebookcount = 0
    twittercount = 0
    instagramcount = 0
    linkedincount = 0
    youtubecount = 0
    tiktokcount = 0
    for method in methods:
        for site in links:
            if site == links[0]:
                if facebookcount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Facebook...\n", 1)
                else:
                    continue
                facebookcount = facebookcount + 1
            elif site == links[1]:
                if twittercount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Twitter...\n", 1)
                else:
                    continue
                twittercount = twittercount + 1
            elif site == links[2]:
                if instagramcount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Instagram...\n", 1)
                else:
                    continue
                instagramcount = instagramcount + 1
            elif site == links[3]:
                if linkedincount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Linkedin...\n", 1)
                else:
                    continue
                linkedincount = linkedincount + 1
            elif site == links[4]:
                if youtubecount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Youtube...\n", 1)
                else:
                    continue
                youtubecount = youtubecount + 1
            elif site == links[5]:
                if tiktokcount == 0:
                    animations.animatetext(f"{CYAN}[+] Scraping Tiktok...\n", 1)
                else:
                    continue
                tiktokcount = tiktokcount + 1
            
            query = f"{method}{name} site:{site}"
            formatter(request_sender(query))
    result = open("results.html", "r").read()
    return result


# main("Byteninja Ethiopia")