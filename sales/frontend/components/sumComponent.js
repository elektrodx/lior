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
		
		event.preventDefault();
		
		$.ajaxSetup({
            headers:
            { 'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content') }
        });
		
		$.ajax({
			url: "/sales/",
			dataType: "json",
			contentType: "application/json; charset=utf-8",
			type: "POST",
			data: { user: 1, amount: 45, payed: 0, pay_date: null, customer: 3 } 
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