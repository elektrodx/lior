/*
 * Modules Dependiencies
 */

import React from 'react';

export default class DescriptionComp extends React.Component{
	render(){		
		return <div>
			<label for="descriptionfield">Descripción: </label><span>{this.props.prod}</span>
			<data id="descriptionfield" value={this.props.prod} />  
		</div>
	}
}