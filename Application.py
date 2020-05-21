from NotVisitedLinks.controller import NotVisitedLinksController
from VisitedLinks.controller import VisitedLinksController
from datetime import datetime
from VisitedLinks.utils import get_server_type
from VisitedLinks.model import VisitedLinksModel


class Application():
    def __init__(self):
        self.visited = VisitedLinksController()
        self.nvisited = NotVisitedLinksController()

    def start(self):
        check_if_empty = self.visited.return_size() + self.nvisited.return_size()
        if check_if_empty is 0:
            start_site = input('Please enter the name of the site you want to start with: ')
            self.nvisited.crawl(start_site)
        while True:
            self.traverse()

    def traverse(self):
        visited_links = []
        nvisited_links = self.nvisited.return_records()
        for link in nvisited_links:
            s_type = get_server_type(link.name)
            nvisited_model = VisitedLinksModel(name=link.name, server_type=s_type, saved=datetime.now())
            visited_links.append(nvisited_model)
            self.nvisited.crawl(link.name)
        self.visited.add_links(visited_links)
