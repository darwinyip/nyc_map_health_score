from flask import jsonify
from app import db

class Restaurant(db.Model):
	camis = db.Column(db.Integer, primary_key=True)
	dba = db.Column(db.String)
	building = db.Column(db.String)
	street = db.Column(db.String)
	boro = db.Column(db.String)
	zipcode = db.Column(db.String)
	cuisine_description = db.Column(db.String)
	phone = db.Column(db.String)
	lat = db.Column(db.Integer)
	lon = db.Column(db.Integer)
	active = db.Column(db.Boolean, default=True)


class Inspection(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	camis = db.Column(db.Integer)
	inspection_date = db.Column(db.Date)
	action = db.Column(db.String)
	violation_code = db.Column(db.String)
	violation_description = db.Column(db.String)
	critical_flag = db.Column(db.String)
	score = db.Column(db.String)
	grade = db.Column(db.String)
	grade_date = db.Column(db.Date)
