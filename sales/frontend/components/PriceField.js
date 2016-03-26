/*
 * Modules Dependiencies
 */

import React from 'react';
import PriceFinal from './PriceFinal';
import CartComponent from './CartComponent';

export default class PriceField extends React.Component{
	constructor(props){
		super(props)
		this.state = { price_base1: 0, productSold: [] }
		this.handleSelect = this.handleSelect.bind(this);
		this.cickEvent = this.cickEvent.bind(this);
	}
	handleSelect (event){
		this.setState({price_base1: event.target.value})
	}
	cickEvent (event){
		event.preventDefault();
		var qty = document.getElementById("qtyField").value;
		this.props.productSold.push(qty);
		if (document.getElementById("PriceField").value == ""){
			document.getElementById("PriceField").value=document.getElementById("PriceField").placeholder
		}
		this.props.productSold.push(document.getElementById("PriceField").value);
		var priceT = document.getElementById("PriceField").value*qty; 
		this.props.productSold.push(priceT.toFixed(2));
		var TproductSold = this.state.productSold;
		TproductSold.push(this.props.productSold);
		this.setState({productSold: TproductSold})
	}

	render(){
		return <div> 
			<select name="pricef" defaultValue={this.props.price_base} onChange={this.handleSelect.bind(this)}>
				<option value={this.props.price_base+(0.30*this.props.price_base)}>Factura</option>
				<option value={this.props.price_base+(0.20*this.props.price_base)}>Sin Factura</option>
				<option value={this.props.price_base+(0.10*this.props.price_base)}>Estuduante</option>
				<option value={this.props.price_base}>Base</option>
			</select>
			<PriceFinal value={this.state.price_base1}/>
			<label for="qtyField">Cantidad:</label>
			<input type="text" id="qtyField"/>
			<button type="submit" onClick={this.cickEvent.bind(this)}>Agregar</button>
			<CartComponent data={this.state.productSold}/>
		</div>
	}
}