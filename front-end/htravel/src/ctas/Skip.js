import React, { Component } from 'react';
import './Skip.css';


class Skip extends Component {
    render() {
        return (
            <div className="skip-all-container">
                <p>or</p>
                <div>
                    <a className="skip-cta" href="#">Skip All</a>
                </div>
            </div>
        );
    }
}

export default Skip;