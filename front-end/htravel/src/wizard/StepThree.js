import React, { Component } from 'react';
// import Next from '../ctas/Next';
import './StepThree.css';

class StepThree extends Component {
    constructor(props) {
        super(props);
    }

    getOptionsElement(options) {
        var mappedOptions = options.map(function(option, index) {
                var discount = option.discount * 100;
    
                if (discount) {
                    discount = <div className="option-discount">{discount + "%"}</div>
                }

                return <article key={index} className="st-option">
                    <div className="st-general-info">
                        {discount}
                        <h3 className="option-name">{option.name}</h3>
                        <p className="cost">{option.cost}</p>
                    </div>
                    <div className="st-option-location">
                        <p className="st-option-origin">{option.origin}</p>
                        <p className="st-option-destination">{option.destination}</p>
                    </div>
                    <div className="st-option-date">
                        <p>{option.departure_date}</p>
                        <p>{option.return_date}</p>
                    </div>
                    <div className="st-option-description">
                        <p>{option.description}</p>
                    </div>
                    <div className="st-option-price">
                        <p>{option.price}</p>
                        <p>{option.cabine}</p>
                    </div>
                    <div className="st-option-cta">
                        <button onClick={(evt) => {this.props.handler('nextBook', this.props.arguments)}}>Comprar Ahora</button>
                    </div>
                </article>
            }.bind(this));

        if (mappedOptions.length > 1) {
            this.setState({apiResponse: mappedOptions});
        }
    }

    getTerms() {
        var terms = this.props.arguments,
            finalString = '';

        for (var i in terms) {
            finalString = finalString + i + '=' + terms[i] + '&';
        }

        return finalString.slice(0, -1)
    }

    componentWillReceiveProps(nextProps) {
        if (nextProps.passedTwo) {
            fetch('http://192.168.43.36:3000/api/?ninguno=0&' + this.getTerms(), 
                { method: 'GET', headers: {
                    "Accept": "application/json"
                }})
                .then((response) => response.json())
                .then((responseJson) => {
                      this.getOptionsElement(responseJson);
                })
                .catch(function(error) {
                    var list = [];

                    list.push(<a href="#" onClick={(evt) => this.props.handler('first', 'reset')}>Volver a intentarlo</a>);

                    this.setState({apiResponse: list});
                }.bind(this));
        }
        
    }

    render() {
        var elements;

        if (this.state &&
            this.state.apiResponse) {
            elements = <div>
                <h5 className="st-title">Te presentamos las siguentes <b>{this.state.apiResponse.length - 1}</b> ofertas que coinciden con tus criterios:</h5>
                    {this.state.apiResponse}
            </div>
        } else {
            elements = <div></div>
        }

        return (
            elements
        );
    }
}

export default StepThree;