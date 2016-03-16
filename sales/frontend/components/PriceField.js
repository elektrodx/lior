/*
 * Modules Dependiencies
 */

import React from 'react';
import PriceFinal from './PriceFinal';
import CartComponent from './CartComponent';

export default class PriceField extends React.Component{
	constructor(props){
		super(props)
		this.state = { price_base1: 0 }
		this.handleSelect = this.handleSelect.bind(this);
	}
	handleSelect (envet){
		this.setState({price_base1: envet.target.value})
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
			<button type="submit">Agregar</button>
			<CartComponent data={this.props.productSold}/>
		</div>
	}
}