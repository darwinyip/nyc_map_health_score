from math import sin, cos, sqrt, atan2, radians
from flask import request, render_template, jsonify
from sqlalchemy import desc, func
from app import app
from .models import Restaurant, Inspection

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/nyc_map_health_score/api/v1/restaurants', methods=['GET'])
def get_restaurants(page=1):
	lat = float(request.args.get('lat'))
	lon = float(request.args.get('lon'))

	restaurants = list(map(row2dict, Restaurant.query
			.filter(
				(Restaurant.lat.isnot(None) | Restaurant.lon.isnot(None))
				& Restaurant.active
				& (func.public.geodistance(lat, lon, Restaurant.lat/1e7, Restaurant.lon/1e7) < 1))
			.paginate(page, 100, False).items))

	restaurants = [{**r, 'lat': r['lat'] / 1e7, 'lon': r['lon'] / 1e7} for r in restaurants]
	response = jsonify(restaurants)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

@app.route('/nyc_map_health_score/api/v1/inspections/<camis>', methods=['GET'])
def get_inspections(camis):
	inspections = list(map(row2dict, Inspection.query
			.filter(Inspection.camis==int(camis))
			.order_by(desc(Inspection.inspection_date))
			.all()))
	response = jsonify(inspections)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)
    return d