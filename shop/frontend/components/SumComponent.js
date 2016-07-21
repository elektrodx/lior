/*
 * Modules Dependiencies
 */

import React from 'react';

var $ = require('jquery');

export default class SumComponent extends React.Component {
	constructor(props){
		super(props)
		this.OnClickEvent = this.OnClickEvent.bind(this);

	}
	OnClickEvent (event){
		var dataj = JSON.stringify(this.props.items)
		var provider = document.getElementById("id_provider")
		var providerN = provider.options[provider.selectedIndex].value
		$.ajax({
			url: '/shops/',
			dataType: 'json',
			type: "POST",
			data:{ 'amount': this.props.sum,
			'price_extra': document.getElementById("id_price_extra").value,
			'total_price': document.getElementById("id_total_price").value,
			'provider': providerN,
			'items': dataj
			},
			statusCode:{
				201: function(){
					location.reload();
				} 
			}
		})
	}
	render(){
		return <div>
			<div>
				<strong>Total Productos:</strong>
				<span>{this.props.sum}</span>
			</div>
			<button className="boton" onClick={this.OnClickEvent.bind(this)}>Procesar</button>
		</div>
	}
}