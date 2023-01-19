from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

startingPage = 'https://mai.ru/'

html = urlopen(startingPage)
bs = BeautifulSoup(html, 'html.parser')

# Retrieves a list of all Internal links found on a page
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if (link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks
urll = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
print(getInternalLinks(bs, urll))