/*
 * Modules Dependiencies
 */

import React from 'react';
import PricetComp from './PricetComp';
import ShopcartComp from './ShopcartComp';

export default class PriceoComp extends React.Component{
	constructor(props){
		super(props)
		this.state = {productshop: [], pricet: 0 }
		this.clickEvent = this.clickEvent.bind(this);
	}

	clickEvent(event){
		event.preventDefault();
		var item = [];
		var array = this.state.productshop;
		item.push(document.getElementById('codeField').value);
		item.push(document.getElementById('descriptionfield').innerHTML);
		item.push(document.getElementById('qtyComp').value);
		item.push(document.getElementById('priceoField').value);
		item.push(Number(document.getElementById('qtyComp').value) * Number(document.getElementById('priceoField').value))
		array.push(item);
		this.setState({productshop: array});

	}

	render(){
		return <div> 
			<div>
				<label for='priceoField'>Precio Unit:</label>
				<input type="text" id="priceoField"/>
				<PricetComp data={this.state.pricet}/>
				<button type="submit" onClick={this.clickEvent.bind(this)}>agregar</button>
			</div>
			<div>
				<ShopcartComp productsshop={this.state.productshop}/>
			</div>
		</div>	
	}
}