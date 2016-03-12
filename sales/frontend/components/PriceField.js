/*
 * Modules Dependiencies
 */

import React from 'react';

export default class PriceField extends React.Component{
	render(){
		return <div> 
			<select>
				<option value="30">Factura</option>
				<option value="20">Sin Factura</option>
				<option value="10">Estuduante</option>
			</select>
			<label for="PriceField">Precio:</label>
			<input type="text" id="PriceField" placeholder={this.props.price_base}/>
		</div>
	}
}