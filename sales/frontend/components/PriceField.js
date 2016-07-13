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
		Number.prototype.round = function(places) {
  			return +(Math.round(this + "e+" + places)  + "e-" + places);
		}
		var price_sellT = event.target.value;
		var price_sell = parseFloat(price_sellT).toFixed(2);
		this.setState({price_base1: price_sell});
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
		document.getElementsByClassName("react-autosuggest")[0].getElementsByTagName("input")[0].value = "";
		document.getElementsByClassName("react-autosuggest")[0].getElementsByTagName("input")[0].autofocus=true;
		document.getElementById("qtyField").value = "";
		document.getElementById("PriceField").value = "";
	}

	render(){
		return <div> 
			<select className="list" name="pricef" onChange={this.handleSelect.bind(this)}>
				<option value="">Elija valor...</option>
				<option value={this.props.price_base/(1-0.50)}>50 %</option>
				<option value={this.props.price_base/(1-0.45)}>45 %</option>
				<option value={this.props.price_base/(1-0.40)}>40 %</option>
				<option value={this.props.price_base/(1-0.35)}>35 %</option>
				<option value={this.props.price_base/(1-0.30)}>30 %</option>
				<option value={this.props.price_base/(1-0.25)}>25 %</option>
				<option value={this.props.price_base/(1-0.20)}>20 %</option>
				<option value={this.props.price_base/(1-0.15)}>15 %</option>
				<option value={this.props.price_base/(1-0.10)}>10 %</option>
				<option value={this.props.price_base}>Precio Base</option>
			</select>
			<PriceFinal value={this.state.price_base1}/>
			<div className="qtyField">
				<label for="qtyField">Cantidad:</label>
				<input type="text" id="qtyField"/>
				<button className="boton" type="submit" onClick={this.cickEvent.bind(this)}>Agregar</button>
			</div>	
			<CartComponent data={this.state.productSold} sum={0}/>
		</div>
	}
}