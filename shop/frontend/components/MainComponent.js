/*
 * Modules Dependiencies
 */

import React from 'react';
import CodigoComp from './CodigoComp';
import QtyComp from './QtyComp';

export default class MainComponent extends React.Component {

	render(){
		return <div>
			<CodigoComp/>
			<QtyComp/>
		</div>
	}

}