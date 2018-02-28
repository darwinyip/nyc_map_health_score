# NYC: Map Health Score

## Introduction
*NYC: Map Health Score* displays NYC restaurant inspection data in a map.

## Components
### ETL
There are 3 main ETL processes:
* Fetch restaurant and inspection data
* Load restaurant and inspection data
* Geocode restaurant data

### Backend
The backend is written in Flask, serving the React page, and the API endpoints. The database is version controlled using Alembic.

### Frontend
The frontend is written in React with 4 components:
* Google Maps that renders the map and the clickable markers denoting the restaurants
* Search Bar which is to search for a location. Example of possible queries are "Central Park", 1 World Trade Center", "Dumbo", or any location searchable through Google Maps.
* Inspection Item contains the inspection details
* Inspection List holds the Inspection Items

For more information, read my [blogpost](http://darwinyip.github.io/2018/02/25/nyc-map-health-score-map.html).
