from sqlalchemy import Column, Integer, String, DateTime
from db.Base import Base


class VisitedLinksModel(Base):
    __tablename__ = "visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    server_type = Column(String)
    saved = Column(DateTime)
