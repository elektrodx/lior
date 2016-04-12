/*
 * Modules Dependiencies
 */

import React from 'react';
import PricetComp from './PricetComp';
import ShopcartComp from './ShopcartComp';

export default class PriceoComp extends React.Component{
	constructor(props){
		super(props)
		this.state = {productshop: [] }
		this.clickEvent = this.clickEvent.bind(this);
	}

	clickEvent(event){
		event.preventDefault();
		var item = [];
		var array = this.state.productshop;
		item.push(document.getElementById('codeField').value);
		item.push(document.getElementById('descriptionfield').innerHTML);
		array.push(item);
		this.setState({productshop: array});

	}

	render(){
		return <div> 
			<div>
				<label for='priceoField'>Precio Unit:</label>
				<input type="text" id="priceoField"/>
				<PricetComp/>
				<button type="submit" onClick={this.clickEvent.bind(this)}>agregar</button>
			</div>
			<div>
				<ShopcartComp productsshop={this.state.productshop}/>
			</div>
		</div>	
	}
}