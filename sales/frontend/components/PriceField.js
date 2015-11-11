/*
 * Modules Dependiencies
 */

import React from 'react';

export default class PriceField extends React.Component{
	render(){
		return <div> 
			<label for="PriceField">Precio:</label>
			<input type="text" id="PriceField" />
		</div>
	}
}