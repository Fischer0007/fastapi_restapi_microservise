
from sqlalchemy import Column, Integer, Float, Date

from db_app.db import Base, engine



class Statistics(Base):
    __tablename__ = "statistics"
    date = Column(Date, primary_key=True)
    views = Column(Integer, nullable=False)
    clicks = Column(Integer, nullable=False)
    cost = Column(Float(precision=2), nullable=False)

    def __str__(self):
        return "{date: '%s', views: '%s', clicks: '%s', cost: '%s', cpc: '%s', cpm: '%s'}" % \
               (self.date, self.views, self.clicks, self.cost,
                round(self.cost/self.clicks, 2), round(self.cost/self.views * 1000, 2)
                )
