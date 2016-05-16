/*
 * Modules Dependiencies
 */

import React from 'react';
import SumComponent from './SumComponent';

export default class CartComponent extends React.Component{
	
	render(){
		return <div className="CartComponent">
			<table className="table-head">
				<tr>
					<th>Codigo</th>
					<th>Descripcion</th>
					<th>Marca</th>
					<th>Cantidad</th>
					<th>Precio Unitario</th>
					<th>Sub total</th>
				</tr>
				{this.props.data.map((item) => {
				this.props.sum = this.props.sum + Number(item[5])
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
		<SumComponent data={this.props.sum}/>
		</div>
	}
}