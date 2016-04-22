/*
 * Modules Dependiencies
 */

import React from 'react';

export default class DescriptionComp extends React.Component{		
	render(){		
		return <div>
			<span id='descriptionfield'>Descripción: {this.props.prod}</span>
		</div>
	}
}