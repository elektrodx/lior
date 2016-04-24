/*
 * Modules Dependiencies
 */

import React from 'react';
import Autosuggest from 'react-autosuggest';
import utils from './../node_modules/react-autosuggest/examples/src/utils.js';
import DescriptionComp from './DescriptionComp';

export default class CodigoComp extends React.Component {
	constructor(props) {
	    super(props)
	    this.state = { productos: [], prods: [], descrip: [] }
	    const suburbs = [];
  	}

	componentWillMount() {
	    fetch('http://127.0.0.1:8000/list_stock/')
	      .then((response) => {
	        return response.json()
	      })
	      .then((productos) => {
	        this.setState({ productos: productos })
	      })
  	}

	getSuggestions(input, callback) {
		// var suggestions = "";
		// console.log(input)
		// fetch('http://127.0.0.1:8000/list_code/'+ input )
	 //      .then((response) => {
	 //        return response.json()
	 //      })
	 //      .then((productos) => {
	 //        this.setState({ productos: productos })
	 //      })
	 //    console.log(this.state.productos)
		const requestDelay = 50 + Math.floor(300 * Math.random());
	    const escapedInput = utils.escapeRegexCharacters(input.trim());
	    const lowercasedInput = input.trim().toLowerCase();
	    const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
	    var suggestions = this.state.productos
	    .filter( suburbObj => suburbMatchRegex.test(' Codigo: ' + suburbObj.code ) )
	    	.sort( (suburbObj1, suburbObj2) =>
	    		suburbObj1.code.toLowerCase().indexOf(lowercasedInput) -
	    		suburbObj2.code.toLowerCase().indexOf(lowercasedInput)
	    	)
	    	.slice(0, 7)
	    	.map( suburbObj => suburbObj.code );
	    console.log(suggestions)
	    var mproduct = []
	    this.state.productos.map((iteme) => {
	    	if (iteme.code == suggestions) {
	    		mproduct.push(iteme.description)
	    		console.log(mproduct)
	    	}
	    })
		this.setState({prods: mproduct })

	    setTimeout(() => callback(null, suggestions), requestDelay);
	}

	render(){
		return <div>
			<label for="codeField">Codigo: </label>
			<Autosuggest suggestions={this.getSuggestions.bind(this)} inputAttributes={{ id: 'codeField' }} />
			<DescriptionComp  prod={this.state.prods}/>
		</div>
	}
}