/*
 * Modules Dependiencies
 */

import React from 'react';
import SumComponent from './SumComponent';
export default class ShopcartComp extends React.Component{
	render(){
		return <div>
			<table className="table-head">
				<th>Código</th>
				<th>Descripción</th>
				<th>Cantidad</th>
				<th>Precio Unitario</th>
				<th>Precio Un. Total</th>
				<th>Precio Ajustado</th>
				<th>Precio Aj. Total</th>
				{this.props.productsshop.map((item) =>{
					this.props.sum = this.props.sum + Number(item[6])
					return <tr>
						<td>{item[0]}</td>
						<td>{item[1]}</td>
						<td>{item[2]}</td>
						<td>{item[3]}</td>
						<td>{item[4]}</td>
						<td className="producto">{item[5]}</td>
						<td>{item[6]}</td>
					</tr>

				})}
			</table>
			<SumComponent sum={this.props.sum} items={this.props.productsshop}/>
		</div>
	}
}