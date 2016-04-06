/*
 * Modules Dependiencies
 */

import React from 'react';
import DescriptionComp from './DescriptionComp'

export default class CodigoComp extends React.Component {
	
	render(){
		return <div>
			<label for="codeField">Codigo: </label>
			<input type="text" id="codeField"/>
			<DescriptionComp/>
		</div>
	}
}