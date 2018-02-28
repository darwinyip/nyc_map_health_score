import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from config import DATABASE, GMAP_API_KEY

OD_BASE_URL = 'https://data.cityofnewyork.us/resource/9w7m-hzhe.json?'
OD_URL_PARAM_LIMIT = '$limit='
OD_URL_PARAM_OFFSET = '$offset='

GMAP_GC_BASE_URL = 'https://maps.googleapis.com/maps/api/geocode/json?address='
GMAP_API_KEY_PARAM = '&key=' + GMAP_API_KEY

engine = create_engine(URL(**DATABASE))

Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()