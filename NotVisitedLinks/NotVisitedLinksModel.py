from sqlalchemy import Column, Integer, String, Boolean
from db.Base import Base


class NotVisitedLinks(Base):
    __tablename__ = "not_visited"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    taken = Column(Boolean)
