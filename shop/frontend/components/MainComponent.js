/*
 * Modules Dependiencies
 */

import React from 'react';
import CodigoComp from './CodigoComp';
import QtyComp from './QtyComp';
import PriceoComp from './PriceoComp';
import ShopcartComp from './ShopcartComp';

export default class MainComponent extends React.Component {

	render(){
		return <div>
			<CodigoComp/>
			<QtyComp/>
			<PriceoComp/>
			<ShopcartComp/>
		</div>
	}

}