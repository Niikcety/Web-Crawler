from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager


Base = declarative_base()
engine = create_engine("sqlite:///urls.db")
Session = sessionmaker(bind=engine)


class VisitedLinks(Base):
    __tablename__ = "visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    server_type = Column(String)
    saved = Column(DateTime)


class NotVisitedLinks(Base):
    __tablename__ = "not_visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    taken = Column(Boolean)


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
