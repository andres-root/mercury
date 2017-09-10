import React, { Component } from 'react';
import FirstStep from './wizard/FirstStep';
import SecondStep from './wizard/StepTwo';
import TirthStep from './wizard/StepThree';
import Menu from './header/Menu';
import SearchBox from './header/SearchBox';
import BookingForm from './wizard/BookinForm';
import Responser from './responses/Responser';
import './App.css';

class App extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            feActive: false,
            seActive: false,
            teActive: false,
            beActive: false,
            resActive: false,
            "arguments": {
                "vacaciones": 0,
                "negocios": 0,
                "aventura": 0,
                "festivales": 0
            },
            passedTwo: false
        };

        this.handler = this.handler.bind(this);
    }

    handler(e, args) {
        if (args !== 'reset') {
            this.setState({arguments: args});
        } else if (args === 'reset') {
        this.setState({"arguments": {
                "vacaciones": 0,
                "negocios": 0,
                "aventura": 0,
                "festivales": 0
            }});
        }

        if (e === 'first' || e === 'reset') {
            this.setState({feActive: false});
            this.setState({seActive: 'active'});
            this.setState({teActive: false});
            this.setState({beActive: false});
            this.setState({resActive: false})
        } else if (e === 'nextThree') {
            this.setState({passedTwo: true});
            this.setState({feActive: false});
            this.setState({seActive: false});
            this.setState({teActive: 'active'});
            this.setState({beActive: false});
            this.setState({resActive: false})
        } else if (e === 'nextBook') {
            this.setState({feActive: false});
            this.setState({seActive: false});
            this.setState({teActive: false});
            this.setState({beActive: 'active'});
            this.setState({resActive: false})
        } else if (e === 'nextPay') {
            this.setState({feActive: false});
            this.setState({seActive: false});
            this.setState({teActive: false});
            this.setState({beActive: false});
            this.setState({resActive: 'active'})
        }
        
    }

    componentDidMount() {
        this.setState({feActive: 'active'})
    } 

    render() {
        return (
            <section>
                <div className="header">
                    <Menu />
                </div>
                <div className="steps">
                    <div className={"first-step " + this.state.feActive}>
                        <FirstStep handler={this.handler.bind(this)} arguments={this.state.arguments} />
                    </div>
                    <div className={"second-step " + this.state.seActive}>
                        <SecondStep handler={this.handler.bind(this)} arguments={this.state.arguments} />
                    </div>
                    <div className={"tirth-step " + this.state.teActive}>
                        <TirthStep handler={this.handler.bind(this)} arguments={this.state.arguments} passedTwo={this.state.passedTwo}/>
                    </div>
                    <div className={"booking-form " + this.state.beActive}>
                        <BookingForm handler={this.handler.bind(this)} />
                    </div>
                    <div className={"greetings " + this.state.resActive}>
                        <Responser handler={this.handler.bind(this)} />
                    </div>
                </div>
            </section>
        );
    }
}


export default App;
