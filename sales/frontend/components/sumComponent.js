/*
 * Modules Dependiencies
 */

import React from 'react';

export default class sumComponent extends React.Component{

	render(){
		return <div className="sumComponent">
			<strong>Precio Total: </strong>
			<span>{this.props.data}</span>
		</div>
	}
}