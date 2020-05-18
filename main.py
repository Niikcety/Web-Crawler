import requests
from bs4 import BeautifulSoup


all_links = []


def crawl(link="https://hackbulgaria.com/"):
    raw_links = []
    try:
        r = requests.get(link, timeout=5)
    except requests.exceptions.ReadTimeout:
        return []
    soup = BeautifulSoup(r.text, features="html.parser")
    for row in soup.find_all('a'):
        link = row.get('href')
        if link is not None and link[0:4] == 'http':
            print(link)
            raw_links.append(link)
    return raw_links


def traverse_through_links(links):
    visited = []
    for link in links:
        if link not in visited:
            visited.append(link)
            links += crawl(link)
    return links


if __name__ == '__main__':
    all_links = traverse_through_links(crawl())
