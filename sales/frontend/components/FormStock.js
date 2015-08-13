/*
 * Modules Dependiencies
 */

import React from 'react';

export default class FormStock extends React.Component{
	render(){
		return <div>
			<label for="StockField">Producto: </label>
			<input type="text" id="StockField" placeholder="Busque el producto"/>
		</div>
	}
}
