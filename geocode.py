from sqlalchemy.orm import load_only
from etl.models import Restaurant, Inspection
from etl import session
from etl.tasks import get_latlong

def main():
	restaurants = []
	try:
		for row in session.query(Restaurant)	\
			.options(load_only('camis','building','street','boro', 'zipcode'))	\
			.filter((Restaurant.lat.is_(None) | Restaurant.lon.is_(None)) & Restaurant.active):
			latlong = get_latlong(' '.join(map(str,[row.building, row.street, row.zipcode])))
			if latlong['status'] == 'ZERO_RESULTS':
				print(row.camis, 'ZERO_RESULTS')
				row.active = False
			else:
				print(row.camis, latlong['lat'], latlong['lng'])
				row.lat = int(latlong['lat'] * 1e7)
				row.lon = int(latlong['lng'] * 1e7)
			restaurants.append(row)
	except Exception as e:
		print("Exception", e)
	finally:
		session.bulk_save_objects(restaurants)
		session.commit()

if __name__ == '__main__':
	main()