import React, { Component } from 'react';

export default class SearchBar extends Component {
	constructor(props) {
		super(props);
		this.state = {search_location: ''};
		this.onInputChange = this.onInputChange.bind(this);
		this.onFormSubmit = this.onFormSubmit.bind(this);
	}

	onInputChange(event) {
		this.setState({search_location: event.target.value});
	}

	onFormSubmit(event) {
		event.preventDefault();
		this.props.onSearchTermChange(this.state.search_location);
		this.setState({ search_location: '' });
	}

	render() {
		return (
			<form className='input-group' onSubmit={this.onFormSubmit}>
				<input
					className='form-control'
					value={this.state.search_location}
					placeholder='search for location...'
					onChange={this.onInputChange}
				/>
			<span className='input-group-btn'>
				<button type='submit' className='btn btn-secondary'>Submit</button>
			</span>
			</form>
		);
	}
}