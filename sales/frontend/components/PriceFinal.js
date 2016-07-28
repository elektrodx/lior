/*
 * Modules Dependiencies
 */
import React from 'react';

export default class PriceFinal extends React.Component{

	render(){
		return <div className="PriceFinal monto">
			<label for="PriceField">Precio:</label>
			<input type="text" id="PriceField" placeholder={this.props.value}/>
		</div>
	}
} 