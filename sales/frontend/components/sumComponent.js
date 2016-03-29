/*
 * Modules Dependiencies
 */

import React from 'react';

export default class sumComponent extends React.Component{

	render(){
		return <div>
			<strong>Total Productos</strong>
			<span>{this.props.data}</span>
		</div>
	}
}