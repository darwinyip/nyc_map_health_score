import React, { Component } from 'react';

export default class GoogleMap extends Component {

	constructor(props) {
		super(props);
		this.state = {
			map: null,
			markers: []
		}

		this.clearMarkers = this.clearMarkers.bind(this);
	}

	componentWillReceiveProps(nextProps) {
		if(this.props.location !== nextProps.location) {
			this.clearMarkers();
		}
	}

	componentDidMount() {
		let map = new window.google.maps.Map(document.getElementById('map'), {
			center: this.props.location,
			zoom: 15
		});

		this.setState({map: map});
	}

	clearMarkers() {
		for(var i = 0; i < this.state.markers.length; i++) {
			this.state.markers[i].setMap(null);
		}
		this.setState({markers: []});
	}

	render() {
		if(this.props.restaurants.length) {
			this.state.map.setCenter(this.props.location);

			this.props.restaurants.map((restaurant) => {
				const marker = new window.google.maps.Marker({
					map: this.state.map,
					position: {lat:restaurant.lat, lng:restaurant.lon}
				});

				this.state.markers.push(marker);

				const contentString = `<h3>${restaurant.dba}</h3>` +
									`<p>${restaurant.building} ${restaurant.street}</br>` +
									`${restaurant.boro} ${restaurant.zipcode}</p>` +
									`<p>Phone: ${restaurant.phone}</p>` +
									`<p>Cuisine: ${restaurant.cuisine_description}</p>`;

				const infoWindow = new window.google.maps.InfoWindow({
					content: contentString
				});

				marker.addListener('click', () => {
					// Hide the previous active InfoWindow
					if(this.state.activeInfoWindow) {
						this.state.activeInfoWindow.close();
					}
					this.setState({activeInfoWindow: infoWindow});
					infoWindow.open(this.state.map, marker);
					this.props.onMarkerSelect(restaurant.camis);
				});

			});
		}

		return (
				<div id='map' />
		);
	}
}