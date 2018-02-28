import React, { Component } from 'react';
import SearchBar from './search_bar';
import GoogleMap from './google_map';
import InspectionList from './inspection_list'
import axios from 'axios';

export default class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			location: {lat: 40.7127753,lng: -74.0059728},
			restaurants: [],
			inspections: []
		 };

		this.searchLocation = this.searchLocation.bind(this);
		this.fetchRestaurants = this.fetchRestaurants.bind(this);
		this.fetchInspections = this.fetchInspections.bind(this);

		this.fetchRestaurants();
	}

	searchLocation(location) {
		const URL = 'https://maps.googleapis.com/maps/api/geocode/json?address=';
		const API_KEY = `&key=${process.env.REACT_APP_GOOGLE_API_KEY}`;
		axios.get(`${URL}${location.replace(' ', '+')}${API_KEY}`)
			.then((response) => {
				this.setState({
					location: response.data.results[0].geometry.location
				});
				this.fetchRestaurants();
			});
	}

	fetchRestaurants() {
		const URL = process.env.REACT_APP_SERVER_URL;
		const API = '/nyc_map_health_score/api/v1/restaurants';
		const PARAMS = `?lat=${this.state.location.lat}&lon=${this.state.location.lng}`;
		axios.get(URL+API+PARAMS)
			.then(response => {
				this.setState({
					restaurants: response.data
			});
		});
	}

	fetchInspections(camis) {
		const URL = process.env.REACT_APP_SERVER_URL;
		const API = `/nyc_map_health_score/api/v1/inspections/${camis}`;
		axios.get(URL+API)
			.then(response => {
				this.setState({
					inspections: response.data
			});
		});
	}

	render() {
		return (
			<div>
				<div className="searchbar">
					<SearchBar onSearchTermChange={this.searchLocation} />
				</div>
				<div className="container">
					<GoogleMap 
						location={this.state.location} 
						restaurants={this.state.restaurants}
						onMarkerSelect={this.fetchInspections} />
					<InspectionList inspections={this.state.inspections} />
				</div>
			</div>
		);
	}
}