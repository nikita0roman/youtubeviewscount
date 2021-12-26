import requests
from bs4 import BeautifulSoup
def couner(link):
    r = requests.get(link)
    src = r.content

    soup = BeautifulSoup(src, "html.parser")

    selectMeta = soup.find('meta', attrs={'itemprop': 'interactionCount'})
    selectMeta

    # searchElement = soup.find ('div', attrs={'itemprop': 'interactionCount'})

    result = str(selectMeta).split('"')[1]
    # print(result)
    return result

# couner("https://www.youtube.com/watch?v=LE9Q4JN-Yek")