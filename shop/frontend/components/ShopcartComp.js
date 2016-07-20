/*
 * Modules Dependiencies
 */

import React from 'react';
import SumComponent from './SumComponent';
export default class ShopcartComp extends React.Component{
	render(){
		return <div>
			<table className="table-head">
				<th>Codigo</th>
				<th>Descripcion</th>
				<th>Cantidad</th>
				<th>precio U</th>
				<th>precio T</th>
				<th>Precio Ajustado</th>
				<th>Precio Ajustado T</th>
				{this.props.productsshop.map((item) =>{
					this.props.sum = this.props.sum + Number(item[6])
					return <tr>
						<td>{item[0]}</td>
						<td>{item[1]}</td>
						<td>{item[2]}</td>
						<td>{item[3]}</td>
						<td>{item[4]}</td>
						<td>{item[5]}</td>
						<td>{item[6]}</td>
					</tr>

				})}
			</table>
			<SumComponent sum={this.props.sum} items={this.props.productsshop}/>
		</div>
	}
}