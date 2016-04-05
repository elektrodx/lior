/*
 * Modules Dependiencies
 */

import React from 'react';

export default class CodigoComp extends React.Component {
	
	render(){
		return <div>
			<label for="codeField">Codigo: </label>
			<input type="text" id="codeField"/>
		</div>
	}
}