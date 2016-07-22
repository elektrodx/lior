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
		document.getElementById('id_provider').disabled = true;
		document.getElementById('id_total_price').disabled = true;
		document.getElementById('id_price_extra').disabled = true;
		// document.getElementById('id_payed').disabled = true;
		// document.getElementById('id_pay_due').disabled = true;
		var item = [];
		var array = this.state.productshop;
		item.push(document.getElementById('codeField').value);
		item.push(document.getElementById('descriptionfield').value);
		item.push(document.getElementById('qtyComp').value);
		item.push(document.getElementById('priceoField').value);
		var pt, ptc, ge, ppt, ppu = 0
		pt = Number(document.getElementById('qtyComp').value) * Number(document.getElementById('priceoField').value);
		ptc = Number(document.getElementById('id_total_price').value);
		ge = Number(document.getElementById('id_price_extra').value);
		item.push(pt.toFixed(2));
		ppt = pt + (( pt/ptc ) * ge);
		ppu = ppt/Number(document.getElementById('qtyComp').value);
		item.push(ppu.toFixed(2));
		item.push(ppt.toFixed(2));
		array.push(item);
		this.setState({productshop: array});
		document.getElementById('codeField').focus();
	}

	render(){
		return <div className="lastcomponent"> 
			<div>
				<label for='priceoField'>Precio Unit:</label>
				<input type="text" id="priceoField"/>
				<PricetComp data={this.state.pricet}/>
				<button className="boton" type="submit" onClick={this.clickEvent.bind(this)}>agregar</button>
			</div>
			<div>
				<ShopcartComp productsshop={this.state.productshop} sum={0}/>
			</div>
		</div>	
	}
}