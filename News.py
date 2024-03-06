import requests
from bs4 import BeautifulSoup
import datetime
from os import system, name 
import locale

locale.getdefaultlocale = (lambda *args: ['en_US', 'utf8'])
TEME = ["Zenica", "Kultura", "Zabava","Politika","Biznis", "Ljudi","Info","Crna Hronika","Sport"]

def local_date_format(x):
    date = str(x.strftime("%d %m %Y"))
    date = date.replace(" ",".") + "."
    return date

# CLEAR SCREEN
def clear(): 
	if name == 'nt': 
		_ = system('cls') 
	else: 
		_ = system('clear') 

# GET TODAY'S DATE IN LOCAL FORMAT
today = datetime.datetime.now().date()
date = local_date_format(today)
#yesterday = local_date_format(today - datetime.timedelta(days=1))

def make_soup_object(url):
    source_code = requests.get(url)
    plain_text = source_code.content
    soup = BeautifulSoup(plain_text, "html.parser") 
    return soup

def get_news(soup):
    articles = soup.find_all("article")
    list_of_articles = []
    for article in articles:
        title = article.find("h2")
        a_tag = title.a
        title = title.text
        link = a_tag.get("href")
        date_of_article = article.find_all("span")[-1].text
        list_of_articles.append([date_of_article, title, link])
    return list_of_articles

def get_news_on(subject):
    url = "https://www.zenicablog.com/category/vijesti/"
    dct = {i:v.lower() for i,v in enumerate(TEME, 1)}
    dct[8] = "crna-hronika"
    url += dct[subject]
    soup = make_soup_object(url)
    return get_news(soup)


def welcome():
    clear()
    # MENI
    while True:
        print("Dobro dosli! O cemu zelite danas citati?")
        for tema in TEME:
            print(TEME.index(tema)+1, "-", tema)
        # ODABIR TEME
        selection = input("Izaberite broj: ")
        while selection not in '123456789': 
            print("Molim vas, ukucajte broj od 1 do 9")
            selection=input()
            continue
        # PRIKAZ TEME
        clear()
        print("The latest news about:", TEME[int(selection)-1])
        get_news_on(int(selection))
        print()
        print()
        # VRACANJE NA GLAVNI MENI
        read_again =input("Pritisnite 'y' da se vratite na pocetni zaslon\n").lower()
        if read_again == "y":
            clear()
        else: break