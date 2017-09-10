import React, { Component } from 'react';
import Next from '../ctas/Next';
import './BookinForm.css';

class BookingForm extends Component {
    constructor(props) {
        super(props);
    }

    setPaymentMethod(evt) {
        var elements = document.getElementsByClassName('pmethod');

        [].forEach.call(elements, function(el) {
            el.classList.remove("active");
        });


        if (evt.target.parentElement.classList[0] === 'pmethod') {
            evt.target.parentElement.classList.toggle('active');
        } else if (evt.target.classList[0] === 'pmethod') {
            evt.target.classList.toggle('active');
        }
    }

    render() {
        return (
            <div>
                <h3 className="bf-title">Datos de Pasajeros</h3>
                <form className="booking-formulary">
                    <div>
                        <label>Tipo de documento</label>
                        <select>
                            <option value="">Cedula de Ciudadania</option>
                            <option value="">Pasaporte</option>
                            <option value="">RUT</option>
                            <option value="">Tarjeta de Identidad</option>
                            <option value="">Cedula de Extranjeria</option>
                            <option value="">Registro civil</option>
                        </select>
                    </div>
                    <div>
                        <label>Numero de identificacion</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Fecha de nacimiento</label>
                        <input type="date" />
                    </div>
                    <div>
                        <label>Nombre</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Apellido</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Email</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Telefono</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Nacionalidad</label>
                        <input type="text" />
                    </div>
                    <div>
                        <label>Fecha de expiracion del pasaporte</label>
                        <input type="date" />
                    </div>
                    <div className="payment">
                        <label>Payment Method</label>
                        <ul className="payment-method-list">
                            <li className="pmethod" onClick={this.setPaymentMethod}>
                                <img src="/images/card2_PSE.png" />
                                <label>PSE</label>
                            </li>
                            <li className="pmethod" onClick={this.setPaymentMethod}>
                                <img src="/images/cards_all.png" />
                                <label>Tarjeta de credito</label>
                            </li>
                            <li className="pmethod" onClick={this.setPaymentMethod}>
                                <img src="/images/icon_cash.png" />
                                <label>Efectivo</label>
                            </li>
                        </ul>
                    </div>
                </form>
                <Next handler={(evt) => {this.props.handler('nextPay', this.props.arguments)}}/>
            </div>
        );
    }
}

export default BookingForm;