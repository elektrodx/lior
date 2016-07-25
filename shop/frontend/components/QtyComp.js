/*
 * Modules Dependiencies
 */

import React from 'react';

export default class QtyComp extends React.Component{
	render(){
		return <div className="separador monto">
			<label for="qtyComp">Cantidad:</label>
			<input type="text" id="qtyComp"/>
		</div>
	}
}