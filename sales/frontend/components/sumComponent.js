/*
 * Modules Dependiencies
 */

import React from 'react';
import jquery from 'jquery';
import TotalPrice from './TotalPrice';

var $ = require('jquery');

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
	OncickEvent (event){
		$.ajax({
			url: "/sales_savejson/",
			dataType: "json",
			type: "POST",
			data: { amount: this.state.amount, customer: 1 } 
			});
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
			<button className="boton padding" onClick={this.OncickEvent.bind(this)} >Procesar</button>	
		</div>
	}
}