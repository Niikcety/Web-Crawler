import requests
from bs4 import BeautifulSoup


raw_links = []
valid_links = []


def crawl(link="https://register.start.bg/"):
    try:
        r = requests.get(link, timeout=5)
    except requests.exceptions.ReadTimeout:
        return []
    soup = BeautifulSoup(r.text, features="html.parser")
    for row in soup.find_all('a'):
        raw_links.append(row.get('href'))
    return raw_links


def parse_crawled(links):
    for link in links:
        if link is not None and link[0:4] == 'http':
            print(link)
            valid_links.append(link)
    return valid_links


if __name__ == '__main__':
    crawled = crawl()
    valid = parse_crawled(crawled)
    for link in valid:
        valid_links += parse_crawled(crawl(link))

