from .model import VisitedLinksModel
from db.db import session_scope
import ipdb

class VisitedLinksGateway():
    def __init__(self):
        self.model = VisitedLinksModel()

    def add_links(self, links):
        ipdb.set_trace()
        with session_scope() as session:
            session.bulk_save_objects(links)

    def size(self):
        size = 0
        with session_scope() as session:
            size = session.query(VisitedLinksModel).count()
        return size
