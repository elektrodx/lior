/*
 * Modules Dependiencies
 */

import React from 'react';
import PricetComp from './PricetComp';

export default class PriceoComp extends React.Component{

	render(){
		return <div>
			<label for='priceoField'>Precio Unit:</label>
			<input type="text" id="priceoField"/>
			<PricetComp/>
		</div>
	}
}