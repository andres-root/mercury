import React, { Component } from 'react';
import './Next.css';

class Next extends Component {
    render() {
        return (
            <div className="next-container">
                <button onClick={this.props.handler} className="cta-next">Siguiente</button>
            </div>
        );
    }
}

export default Next;