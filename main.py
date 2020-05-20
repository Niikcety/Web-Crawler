import requests
from bs4 import BeautifulSoup
from db import session, VisitedLinks, NotVisitedLinks


def crawl(link="https://register.start.bg/"):
    queue_links = []
    try:
        r = requests.get(link, timeout=5)
    except Exception:
        return
    soup = BeautifulSoup(r.text, features="html.parser")
    for row in soup.find_all('a'):
        link_row = row.get('href')
        if link_row is not None:
            if link_row[0:4] == 'http':
                queue_links.append(NotVisitedLinks(name=link_row))
            elif link_row[0:4] == 'link':
                queue_links.append(NotVisitedLinks(name=link + link_row))
    session.add_all(queue_links)
    session.commit()


def get_server_type(link):
    try:
        r = requests.head(link, timeout=5)
        return r.headers['Server']
    except Exception:
        return 'Unknown'


def check_if_not_visited(link):
    visited = session.query(VisitedLinks).filter(VisitedLinks.name == link)
    try:
        visited.name
    except AttributeError:
        return True
    return False


def traverse_through_links():
    while True:
        first_in_queue = session.query(NotVisitedLinks).first()
        if check_if_not_visited(first_in_queue.name):
            visited = VisitedLinks(name=first_in_queue.name, server_type=get_server_type(first_in_queue.name))
            session.add(visited)
            session.commit()
            crawl(first_in_queue.name)
        session.delete(first_in_queue)
        session.commit()


def check_if_db_is_empty():
    visited_count = session.query(VisitedLinks).count()
    not_visited_count = session.query(NotVisitedLinks).count()

    return (visited_count + not_visited_count == 0, visited_count, not_visited_count)


def start():
    check_if_empty = check_if_db_is_empty()
    if check_if_empty[0]:
        name_of_crawl_start = input('Please enter the name of the site you want to crawl: ')
        crawl(name_of_crawl_start)
    else:
        print('They are {} visited sites and {} in the queue'.format(check_if_empty[1], check_if_empty[2]))
    traverse_through_links()


if __name__ == '__main__':
    start()

