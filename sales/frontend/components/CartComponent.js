/*
 * Modules Dependiencies
 */

import React from 'react';

export default class CartComponent extends React.Component{

	render(){
		return <table>
			<tr>
				<th>Codigo</th>
				<th>Descripcion</th>
				<th>Marca</th>
				<th>Cantidad</th>

			</tr>
			<tr>
				<td>{this.props.data[0]}</td>
				<td>{this.props.data[1]}</td>
				<td>{this.props.data[2]}</td>
				
			</tr>		
		</table>
	}
}