from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime


Base = declarative_base()
engine = create_engine("sqlite:///database/currency.db")


class DailyDigitalCurrency(Base):
    __tablename__ = "DAILY_DIGITAL_CURRENCY"
    id = Column(Integer, primary_key=True)
    open = Column(Float(precision=8))
    high = Column(Float(precision=8))
    low = Column(Float(precision=8))
    close = Column(Float(precision=8))
    volume = Column(Float(precision=8))
    market_cap = Column(Float(precision=8))
    date = Column(DateTime)
    year = Column(Integer)
    iso_week = Column(Integer)

    def __init__(self, name, open, high, low, close, volume, market_cap, date):
        self.name = name
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.market_cap = market_cap
        self.date = date
        self.year = date.year
        self.iso_week = date.isocalendar()[1]

    def __init__(self, kwargs):
        self.name = kwargs.get("name")
        self.open = kwargs.get("open")
        self.high = kwargs.get("high")
        self.low = kwargs.get("low")
        self.close = kwargs.get("close")
        self.volume = kwargs.get("volume")
        self.market_cap = kwargs.get("market_cap")
        date = kwargs.get("date")
        self.date = date
        self.year = date.year
        self.iso_week = date.isocalendar()[1]


def create_tables():
    _db_session = sessionmaker(engine)()
    Base.metadata.create_all(engine)
    _db_session.commit()


def drop_tables():
    for tbl in reversed(Base.metadata.sorted_tables):
        tbl.drop(engine, checkfirst=True)


def insert(daily_digital_currency):
    _db_session = sessionmaker(engine)()
    _db_session.add(daily_digital_currency)
    _db_session.commit()


def get_latest_date():
    _db_session = sessionmaker(engine)()
    # Get the Higher date
    result = _db_session.execute(
        "SELECT date FROM `DAILY_DIGITAL_CURRENCY` ORDER BY date DESC LIMIT 1;"
    ).first()
    if result is None:
        return None
    # return resulted query
    return datetime.strptime(result[0], "%Y-%m-%d %H:%M:%S.%f")


def select(query):
    _db_session = sessionmaker(engine)()
    # Get the Higher date
    result = _db_session.execute(query)
    # return resulted query
    return result
