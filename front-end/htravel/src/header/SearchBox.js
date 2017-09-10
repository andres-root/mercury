import React, { Component } from 'react';
import PlacesAutocomplete, { geocodeByAddress, getLatLng } from 'react-places-autocomplete';
import './SearchBox.css';

class SearchBox extends Component {
    constructor(props) {
        super(props);
        this.state = {address: ''};
        this.onChange = (address) => this.setState({ address });
    }

    handleFormSubmit = (event) => {
        event.preventDefault()

        geocodeByAddress(this.state.address)
          .then(results => getLatLng(results[0]))
          .then(latLng => console.log('Success', latLng))
          .catch(error => console.error('Error', error))
    }

    handleEnter = (address) => {
        geocodeByAddress(address)
        .then(results => {
            console.log('results', results)
        })
    }

    render() {
        const inputProps = {
            value: this.state.address,
            onChange: this.onChange,
            placeholder: 'Busca tu destino!'
        };


        return (
            <form onSubmit={this.handleFormSubmit}>
                <PlacesAutocomplete inputProps={inputProps} className='search-box-input' onEnterKeyDown={this.handleEnter}/>
            </form>
        )
    }
}

export default SearchBox;