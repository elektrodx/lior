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
				<th>Precio Unitario</th>
				<th>Precio total</th>

			</tr>
			{this.props.data.map((item) => { 
			return 	<tr>
					<td>{item[0]}</td>
					<td>{item[1]}</td>
					<td>{item[2]}</td>
					<td>{item[3]}</td>
					<td>{item[4]}</td>
					<td>{item[5]}</td>
				</tr>						
				})
			}
		</table>
	}
}