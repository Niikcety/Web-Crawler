import requests
from bs4 import BeautifulSoup
from db import Base, session, Links


all_links = []


def crawl(link="https://register.start.bg/"):
    raw_links = []
    try:
        r = requests.get(link, timeout=5)
    except requests.exceptions.ReadTimeout:
        return []
    soup = BeautifulSoup(r.text, features="html.parser")
    for row in soup.find_all('a'):
        link = row.get('href')
        if link is not None and link[0:4] == 'http':
            raw_links.append(link)
    return raw_links


def get_server_type(link):
    try:
        r = requests.head(link, timeout=5)
        return r.headers['Server']
    except Exception:
        return 'Unknown'


def traverse_through_links(links):
    visited = []
    for link in links:
        if link not in visited:
            session.add(Links(name=link, server_type=get_server_type(link)))
            session.commit()
            visited.append(link)
            links += crawl(link)
    return links


if __name__ == '__main__':
    start_links = crawl()
    traverse_through_links(start_links)
