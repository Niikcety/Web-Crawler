from .model import NotVisitedLinksModel
from db.db import session_scope, engine, UPDATE_ALL


class NotVisitedLinksGateway():
    def __init__(self):
        self.model = NotVisitedLinksModel()

    def crawl(self, queue_links):
        with session_scope() as session:
            session.add_all(queue_links)

    def update_records(self, records):
        with engine.connect() as conn:
            conn.execute(UPDATE_ALL, (records[0].id, records[19].id))

    def return_records(self):
        with session_scope() as session:
            records = session.query(NotVisitedLinksModel).filter(NotVisitedLinksModel.taken == False).limit(20).all()
        return records

    def size(self):
        size = 0
        with session_scope() as session:
            size = session.query(NotVisitedLinksModel).count()
        return size
