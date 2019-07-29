from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from coast.settings import get_logger

LOGGER = get_logger()
Base = declarative_base()
engine = create_engine(
    "sqlite:///database/currency.db", connect_args={"check_same_thread": False}
)


class DailyDigitalCurrency(Base):
    """
    Model class for SQLite
    """
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

    def __init__(self, dict_values):
        """
        @param dict_values: dictionary with keys: `name`, `open`, `high`, `close`, `volume`, `market_cap`, `date`
        """
        try:
            self.name = dict_values.get("name")
            self.open = dict_values.get("open")
            self.high = dict_values.get("high")
            self.low = dict_values.get("low")
            self.close = dict_values.get("close")
            self.volume = dict_values.get("volume")
            self.market_cap = dict_values.get("market_cap")
            date = dict_values.get("date")
            self.date = date
            self.year = date.year
            self.iso_week = date.isocalendar()[1]
        except KeyError as e:
            LOGGER.error("Key {} was not in dictionary".format(e))
            raise


def create_tables():
    """
    Method to Create all tables
    """
    try:
        LOGGER.debug("Start create all tables")
        _db_session = sessionmaker(engine)()
        Base.metadata.create_all(engine)
        _db_session.commit()
    except Exception as e:
        LOGGER.error("Error while creating tables\n{}".format(e))
        raise


def drop_tables():
    """
    Method to DROP all tables
    """
    try:
        LOGGER.debug("Start dropping tables")
        for tbl in reversed(Base.metadata.sorted_tables):
            tbl.drop(engine, checkfirst=True)
    except Exception as e:
        LOGGER.error("Error while dropping tables\n{}".format(e))
        raise


def insert(daily_digital_currency):
    """
    Method to insert data
    """
    try:
        LOGGER.debug("Inserting data")
        _db_session = sessionmaker(engine)()
        _db_session.add(daily_digital_currency)
        _db_session.commit()
    except Exception as e:
        LOGGER.error("Error while inserting data: {}".format(e))
        raise


def get_latest_date():
    """
    Method to get the latest date
    @return: the higher date from TABLE DAILY_DIGITAL_CURRENCY
    """
    LOGGER.debug("Collecting the higher date from table DAILY_DIGITAL_CURRENCY")
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
    """
    Method to execute query
    @return: the result of query
    """
    try:
        LOGGER.debug("Executing query:\n[{}]".format(query))
        _db_session = sessionmaker(engine)()
        # Get the Higher date
        result = _db_session.execute(query)
    except Exception as e:
        LOGGER.error("Error while executing query:\n[{}]".format(e))
        raise

    # return resulted query
    return result
