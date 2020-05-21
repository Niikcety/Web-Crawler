from .model import NotVisitedLinksModel


def sort_links(soup, link):
    queue_links = []
    for row in soup.find_all('a'):
        link_row = row.get('href')
        if link_row is not None and link_row[0:4] == 'http':
            queue_links.append(NotVisitedLinksModel(name=link_row, taken=False))
        elif link_row is not None and link_row[0:4] == 'link':
            queue_links.append(NotVisitedLinksModel(name=link + link_row, taken=False))
    return queue_links
