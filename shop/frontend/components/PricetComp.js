/*
 * Modules Dependiencies
 */

import React from 'react';

export default class PricetComp extends React.Component{
	
	render(){
		return <div>
		<span>Precio Total: {this.props.data}</span>
		</div>
	}
}