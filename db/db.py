from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from VisitedLinks.model import VisitedLinksModel
from NotVisitedLinks.model import NotVisitedLinksModel
from .Base import Base


engine = create_engine("sqlite:///urls.db")
Session = sessionmaker(bind=engine)


@contextmanager
def session_scope():
    session = Session()
    session.expire_on_commit = False
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


Base.metadata.create_all(engine)

UPDATE_ALL = """UPDATE not_visited SET taken = True WHERE id >= (?) AND id <= (?);"""
GET_ALL_SERVER_TYPES_BY_TIME_INTERVAL = """ SELECT server_type, COUNT(server_type) FROM visited WHERE
                                         saved BETWEEN (?) AND (?) GROUP BY server_type """
