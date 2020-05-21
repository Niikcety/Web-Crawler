from .gateway import VisitedLinksGateway


class VisitedLinksController:
    def __init__(self):
        self.gateway = VisitedLinksGateway()

    def add_links(self, links):
        self.gateway.add_links(links)

    def return_size(self):
        return self.gateway.size()

