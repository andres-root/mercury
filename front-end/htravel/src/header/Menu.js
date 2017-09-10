import React, { Component } from 'react';
import './Menu.css';

class Menu extends Component {
    getMenuElements() {
        var menuElements = [
            {
                "label": "Promociones",
                "url": "https://www.google.com.co/",
                "target": "_blank"
            },{
                "label": "Acerca de",
                "url": "https://www.google.com.co/",
                "target": "_blank"
            },{
                "label": "Fatal Error",
                "url": "https://www.google.com.co/",
                "target": "_blank"
            },
        ];
        return menuElements.map((el, i) => {
            return <li key={i} className="menu-element">
                <a href={el.url} target={el.target}>el.label</a>
            </li>
        });
    }

    toggleMenu(evt) {

    }

    render() {
        var menuElements = this.getMenuElements();

        return (
            <div>
                <div className="header-icon"></div>
                <ul className="menu-list">
                    <li className="menu-hamburguer">
                        <a className="menu-hamburguer-link icon-menu" href="#" target="_self" onClick={(evt) => this.toggleMenu(evt)}></a>
                    </li>
                    {menuElements}
                </ul>
            </div>
        );
    }
}

export default Menu;