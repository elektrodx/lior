/*
 * Modules Dependiencies
 */

import React from 'react';
import TotalPrice from './TotalPrice';

export default class sumComponent extends React.Component{
	constructor(props){
		super(props)
		this.state = { amount: 0 }
		this.eventKeyPress = this.eventKeyPress.bind(this);
	}

	eventKeyPress (event) {
		var sum = Number(this.props.data) - Number(document.getElementById("descAmount").value);
		console.log(sum)
		this.setState({ amount: sum })
	}

	render(){
		return <div className="sumComponent">
			<div>
				<strong>Total Productos: </strong>
				<span>{this.props.data}</span>
			</div>
			<div>
				<label for="descAmount">Descuento: </label>
				<input type="number" id="descAmount" onKeyUp={this.eventKeyPress.bind(this)}/>
			</div>
			<TotalPrice amount={this.state.amount}/>
			<button className="boton padding">Procesar</button>	
		</div>
	}
}