 /*
 * Modules Dependiencies
 */

import React from 'react';

export default class TotalPrice extends React.Component{
	
	render(){
		return <div>
			<strong>Total A Pagar: </strong>
			<strong><span>{this.props.amount}</span></strong>
		</div>
	}
}
