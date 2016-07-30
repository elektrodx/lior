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
		// console.log(sum)
		this.setState({ amount: sum })
	}
	OncickEvent (event){
		event.preventDefault();
		var dataj = JSON.stringify(this.props.items)
		$.ajax({
			url: '/sales/',
			dataType: 'json',
			type: "POST",
			data: { 'amount': this.state.amount,
			 'customer': document.getElementById("ClientCI").value,
			 'items':  dataj
			 }, 
			 statusCode: {
    			201: function() {
      				// location.reload();
      				window.location = "/invoice/"
    				},
    			500: function()	{
    				alert("Existe un Error en su Solicitud")
    				}
  				}
			});
	}
	render(){
		return <div className="sumComponent">
			<div>
				<strong>Total Productos: </strong>
				<span>{this.props.data}</span>
			</div>
			<div className="monto">
				<label for="descAmount">Descuento: </label>
				<input type="number" step="0.01" id="descAmount" onKeyUp={this.eventKeyPress.bind(this)}/>
			</div>
			<TotalPrice amount={this.state.amount}/>
			<button className="boton padding" onClick={this.OncickEvent.bind(this)} >Procesar</button>	
		</div>
	}
}