from .gateway import NotVisitedLinksGateway
from .utils import sort_links
from bs4 import BeautifulSoup
import requests
import time


class NotVisitedLinksController():
    def __init__(self):
        self.gateway = NotVisitedLinksGateway()

    def crawl(self, link="https://register.start.bg/"):
        try:
            r = requests.get(link, timeout=5)
        except Exception:
            return
        soup = BeautifulSoup(r.text, features="html.parser")

        sorted_links = sort_links(soup, link)
        self.gateway.crawl(sorted_links)

    def return_records(self):
        records = self.gateway.return_records()

        if len(records) is 20:
            self.gateway.update_records(records)
            return records

        time.sleep(3)
        self.return_records()

    def return_size(self):
        return self.gateway.size()
