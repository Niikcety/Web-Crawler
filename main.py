import requests
from bs4 import BeautifulSoup
from db.db import session_scope, VisitedLinks, NotVisitedLinks, engine, UPDATE_ALL
import datetime
import time


def crawl(link="https://register.start.bg/"):
    queue_links = []
    try:
        r = requests.get(link, timeout=5)
    except Exception:
        return
    soup = BeautifulSoup(r.text, features="html.parser")
    for row in soup.find_all('a'):
        link_row = row.get('href')
        if link_row is not None and link_row[0:4] == 'http':
            queue_links.append(NotVisitedLinks(name=link_row, taken=False))
        elif link_row is not None and link_row[0:4] == 'link':
            queue_links.append(NotVisitedLinks(name=link + link_row, taken=False))
    with session_scope() as session:
        session.add_all(queue_links)


def get_server_type(link):
    try:
        r = requests.head(link, timeout=5)
        return r.headers['Server']
    except Exception:
        return 'Unknown'


def traverse_through_links(links):
    visited_links = []
    update_hundread_records(links)
    for link in links:
        print(link.name)
        visited = VisitedLinks(name=link.name,
                               server_type=get_server_type(link.name), saved=datetime.datetime.now())
        visited_links.append(visited)
        crawl(link.name)
    with session_scope() as session:
        session.add_all(visited_links)


def check_if_db_is_empty():
    with session_scope() as session:
        visited_count = session.query(VisitedLinks).count()
        not_visited_count = session.query(NotVisitedLinks).count()

    return (visited_count + not_visited_count == 0, visited_count, not_visited_count)


def update_hundread_records(records):
    with engine.connect() as conn:
        conn.execute(UPDATE_ALL, (records[0].id, records[19].id))


def return_hundread_records():
    with session_scope() as session:
        records = session.query(NotVisitedLinks).filter(NotVisitedLinks.taken == False).limit(20).all()
    if len(records) is 20:
        return records
    time.sleep(3)
    return_hundread_records()


def start():
    check_if_empty = check_if_db_is_empty()
    if check_if_empty[0]:
        name_of_crawl_start = input('Please enter the name of the site you want to crawl: ')
        crawl(name_of_crawl_start)
    try:
        while True:
            traverse_through_links(return_hundread_records())
    except KeyboardInterrupt:
        print("Bye Bye")


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        pass
