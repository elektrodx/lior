/*
 * Modules Dependiencies
 */

import React from 'react';

export default class FormListStock extends React.Component{
	render(){
		return <datalist id="stocklist">
		{
      	this.props.opciones.map((order) => {
      		let coptions = order.description + " " + order.brand + " " + order.qty
		return <option value={coptions}/>
		})
      	}
		</datalist>
		}
	}