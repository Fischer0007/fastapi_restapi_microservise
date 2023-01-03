
from sqlalchemy import Column, Integer, Float, Date

from db_app.db import Base


class Statistics(Base):
    __tablename__ = "statistics"
    date = Column(Date, primary_key=True)
    views = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Float(precision=2), nullable=False)
