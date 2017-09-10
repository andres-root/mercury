import React, { Component } from 'react';
import Next from '../ctas/Next';
import './StepTwo.css';

class StepTwo extends Component {
    constructor(props) {
        super(props);
    }

    handleClick = function(evt, type) {
        if (evt.target.parentElement.classList[0] === 'ss-option') {
            evt.target.parentElement.classList.toggle('active');
        } else if (evt.target.classList[0] === 'ss-option') {
            evt.target.classList.toggle('active');
        }

        this.props.arguments[type]++
    }

    getOptionsElement() {
        var options = this.getOptions();

        return options.map((option, index) => {
            return <li key={index} className="ss-option" onClick={(evt) => this.handleClick(evt, option.type)}>
                <img src={option.src} alt={options.label} />
            </li>
        });
    }

    getOptions() {
        return [
            {
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "Paris",
                "type": "vacaciones"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "Roma",
                "type": "negocios"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "Berlin",
                "type": "negocios"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "Yolo",
                "type": "vacaciones"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "A1",
                "type": "negocios"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "B1",
                "type": "negocios"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "A2",
                "type": "aventura"
            },{
                "src": "https://dummyimage.com/100x100/000/fff.jpg",
                "label": "B2",
                "type": "festivales"
            }
        ]
    }

    render() {
        var optionsEl = this.getOptionsElement();

        return (
            <div>
                <h2 className="ss-title">Con que te sientes familiarizado?</h2>
                <ul className="ss-container">
                    {optionsEl}
                </ul>
                <Next handler={(evt) => {this.props.handler('nextThree', this.props.arguments)}} />
            </div>
        );
    }
}

export default StepTwo;