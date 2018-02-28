from json import loads
from urllib.request import urlopen
from .models import Restaurant, Inspection
from etl import OD_BASE_URL, OD_URL_PARAM_LIMIT, OD_URL_PARAM_OFFSET, session

def json_generator(url, offset=1000):
	current_offset = 0
	result_length = None
	while result_length == offset or result_length is None:
		print(url+'&'+OD_URL_PARAM_LIMIT+str(offset)+'&'+OD_URL_PARAM_OFFSET+str(current_offset))
		json_out = None
		try:
			json_url = urlopen(url+'&'+OD_URL_PARAM_LIMIT+str(offset)+'&'+OD_URL_PARAM_OFFSET+str(current_offset))
			json_out = loads(json_url.read())
			yield json_out
		except Exception as e:
			print(e)
		result_length = len(json_out)
		current_offset += offset

def fetch_restaurant_data(camis=None):
	URL = OD_BASE_URL + '$select=distinct%20' + ','.join(list(Restaurant.__table__.columns.keys()))
	if camis:
		URL += '&$where=camis=\'' + camis + '\''
	return json_generator(URL)

def fetch_inspection_data(camis=None):
	URL = OD_BASE_URL + '$select=' + ','.join(list(Inspection.__table__.columns.keys())[1:])
	if camis:
		URL += '&$where=camis=\'' + camis + '\''
	return json_generator(URL)

def bulk_load_restaurant_data():
	for json in fetch_restaurant_data():
		restaurants = [Restaurant(**restaurant) for restaurant in json]
		try:
			session.bulk_save_objects(restaurants)
			session.commit()
		except Exception as e:
			print(e)
			session.rollback()
				
def bulk_load_inspection_data():
	for json in fetch_inspection_data():
		inspections = [Inspection(**inspection) for inspection in json]
		try:
			session.bulk_save_objects(inspections)
			session.commit()
		except Exception as e:
			print(e)
			session.rollback()
	
def main():
	bulk_load_restaurant_data()
	bulk_load_inspection_data()

if __name__ == '__main__':
	main()

# session.close()
