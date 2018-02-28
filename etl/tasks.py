from json import loads
from urllib.request import urlopen
from sqlalchemy import update
from etl import GMAP_GC_BASE_URL, GMAP_API_KEY_PARAM

# TODO: Improve status handling
def get_latlong(address):
	url = GMAP_GC_BASE_URL + address.replace(' ', '%20') + GMAP_API_KEY_PARAM
	print(url)
	json_url = urlopen(url)
	json_out = loads(json_url.read().decode('utf8'))
	if json_out['status'] == 'OK':
		latlong = json_out['results'][0]['geometry']['location']
		latlong.update({'status': 'OK'})
		return latlong
	elif json_out['status'] == 'ZERO_RESULTS':
		return {'status': 'ZERO_RESULTS'}
	else:
		return {'status': 'TERMINATED'}

