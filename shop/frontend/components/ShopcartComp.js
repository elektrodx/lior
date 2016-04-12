/*
 * Modules Dependiencies
 */

import React from 'react';
export default class ShopcartComp extends React.Component{
	render(){
		return <div>
			<table>
				<th>Codigo</th>
				<th>Descripcion</th>
				<th>Cantidad</th>
				<th>precio U</th>
				<th>precio T</th>
				<th>Precio Ajustado</th>
				{this.props.productsshop.map((item) =>{
					return <tr>
						<td>{item[0]}</td>
						<td>{item[1]}</td>
						<td>{item[2]}</td>
						<td>{item[3]}</td>
						<td>{item[4]}</td>
						<td>{item[5]}</td>
					</tr>

				})}
			</table>
		</div>
	}
}