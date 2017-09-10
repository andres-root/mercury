import React, { Component } from 'react';
import Next from '../ctas/Next';
import Skip from '../ctas/Skip';
import './FirstStep.css';

class FirstStep extends Component {
    constructor(props) {
        super(props);
        this.state = {selectedCats: []};
    }

    handleClick = function(evt, type) {
        if (evt.target.parentElement.classList[0] === 'fs-option') {
            evt.target.parentElement.classList.toggle('active');
        } else if (evt.target.classList[0] === 'fs-option') {
            evt.target.classList.toggle('active');
        }

        this.props.arguments[type]++
    }

    getOptionsElement() {
        var options = this.getOptions();

        return options.map((option, index) => {
            return <li 
                className={"fs-option " + option.class}
                key={index}
                onClick={(evt) => this.handleClick(evt, option.type)}
                >
                    <span className="fs-option-text">{option.name}</span>
                    <div className="fs-option-circle"></div>
                </li>
        });
    }

    getOptions() {
        return [
            {
                "name": "Vacaciones",
                "class": "icon-local_hotel",
                "type": "vacaciones"
            },
            {
                "name": "Negocios",
                "class": "icon-work",
                "type": "negocios"

            },
            {
                "name": "Aventura",
                "class": "icon-terrain",
                "type": "aventura"

            },
            {
                "name": "Festivales",
                "class": "icon-radio",
                "type": "festivales"

            }
        ]
    }

    render() {
        var optionsEl = this.getOptionsElement();

        return (
            <div>
                <h2 className="fs-title">Selecciona tus intereses</h2>
                <ul className="fs-options">
                    {optionsEl}
                </ul>
                <Next handler={(e) => this.props.handler('first', this.props.arguments)}/>
            </div>
        );
    }
}

export default FirstStep;