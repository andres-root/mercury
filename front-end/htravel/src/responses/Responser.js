import React, { Component } from 'react';
import './Response.css';

class Responser extends Component {
    render() {
        return (
            <article className="payment-complete">
                <div className="circle"><p className="check"></p></div>
                <p className="greetings-message">Tu pago ha sido exitoso. Disfruta tu viaje :)</p>
                <form>
                    <button>Volver al inicio</button>
                </form>
            </article>
        )
    }
};

export default Responser;