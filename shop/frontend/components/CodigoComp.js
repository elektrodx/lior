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
	    this.state = { productos: [], prods: [] }
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
		const requestDelay = 50 + Math.floor(300 * Math.random());
	    const escapedInput = utils.escapeRegexCharacters(input.trim());
	    const lowercasedInput = input.trim().toLowerCase();
	    const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
	    const suggestions = this.state.productos
	    .filter( suburbObj => suburbMatchRegex.test(' Codigo: ' + suburbObj.code) )
	    	.sort( (suburbObj1, suburbObj2) =>
	    		suburbObj1.code.toLowerCase().indexOf(lowercasedInput) -
	    		suburbObj2.code.toLowerCase().indexOf(lowercasedInput)
	    	)
	    	.slice(0, 7)
	    	.map( suburbObj => suburbObj.code );

	    setTimeout(() => callback(null, suggestions), requestDelay);

	    var mproduct = []
	    console.log(suggestions)
	    this.state.productos.map((iteme) => {
	    	if (iteme.code == suggestions) {
	    		mproduct.push(iteme.description)
	    		console.log(mproduct)
	    	};
	    })
		this.setState({prods: mproduct })
	}

	// renderSuggestion(suggestionObj, input) {
	//     const escapedInput = utils.escapeRegexCharacters(input);
	//     const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
	//     const suggestion = 'Codigo: ' + suggestionObj.code;
	//     const firstMatchIndex = suggestion.search(suburbMatchRegex);

	//     if (firstMatchIndex === -1) {
	//       return suggestion;
	//     }

	//     const beforeMatch = suggestion.slice(0, firstMatchIndex);
	//     const match = suggestion.slice(firstMatchIndex, firstMatchIndex + input.length);
	//     const afterMatch = suggestion.slice(firstMatchIndex + input.length);

	//     return (
	//       <span>
	//         {beforeMatch}<strong>{match}</strong>{afterMatch}<br />
	//         <small style={{ color: '#777' }}>Descripcion: {suggestionObj.description}</small>
	//       </span>
	//     );
	// }

	// getSuggestionValue(suggestion) { 
	// 	var mproduct = []
	// 	mproduct.push(suggestion.description)
	// 	console.log(mproduct)
	// 	debugger
	// 	this.setState({prods: mproduct })
	// 	return suggestion.code;
	// }

	render(){
		return <div>
			<label for="codeField">Codigo: </label>
			<Autosuggest suggestions={this.getSuggestions.bind(this)} inputAttributes={{ id: 'codeField' }} />
			<DescriptionComp  prod={this.state.prods}/>
		</div>
	}
}