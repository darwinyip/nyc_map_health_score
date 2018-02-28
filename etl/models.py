from sqlalchemy import Column, Integer, String, Date, Boolean
from etl import Base

class Restaurant(Base):
	__tablename__ = 'restaurant'

	camis = Column(Integer, primary_key=True)
	dba = Column(String)
	building = Column(String)
	street = Column(String)
	boro = Column(String)
	zipcode = Column(String)
	cuisine_description = Column(String)
	phone = Column(String)
	lat = Column(Integer)
	lon = Column(Integer)
	active = Column(Boolean, default=True)

	def __init__(self, **entries):
		self.__dict__.update(entries)

class Inspection(Base):
	__tablename__ = 'inspection'

	id = Column(Integer, primary_key=True)
	camis = Column(Integer)
	inspection_date = Column(Date)
	action = Column(String)
	violation_code = Column(String)
	violation_description = Column(String)
	critical_flag = Column(String)
	score = Column(String)
	grade = Column(String)
	grade_date = Column(Date)

	def __init__(self, **entries):
		self.__dict__.update(entries)