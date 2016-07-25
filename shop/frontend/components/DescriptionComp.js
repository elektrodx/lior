/*
 * Modules Dependiencies
 */

import React from 'react';

export default class DescriptionComp extends React.Component{
	render(){		
		return <div>
			<label for="descriptionfield">Descripción del producto: </label><span className="producto">{this.props.prod}</span>
			<data id="descriptionfield" value={this.props.prod} />
		</div>
	}
}