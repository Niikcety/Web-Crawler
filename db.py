from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class VisitedLinks(Base):
    __tablename__ = "visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    server_type = Column(String)


class NotVisitedLinks(Base):
    __tablename__ = "not_visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine("sqlite:///urls.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()
