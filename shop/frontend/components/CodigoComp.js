/*
 * Modules Dependiencies
 */

import React from 'react';
import Autosuggest from 'react-autosuggest';
import utils from '../node_modules/react-autosuggest/examples/src/utils.js';
import DescriptionComp from './DescriptionComp';

export default class CodigoComp extends React.Component {
	constructor(props) {
	    super(props)
	    this.state = { productos: [], prods: [], descrip: [] }
	    const suburbs = [];
  	}

	componentWillMount() {
	    fetch('http://lior.omcor.us/list_stock/')
	      .then((response) => {
	        return response.json()
	      })
	      .then((productos) => {
	        this.setState({ productos: productos })
	      })
  	}

  	population(suburbObj) {
  	  return suburbObj.description.split('').reduce((result, char) => result + char.charCodeAt(0), 0) +
  	       +suburbObj.brand.split('').reverse().join('');
  	}

  	getSuggestions(input, callback) {
  	  const requestDelay = 50 + Math.floor(300 * Math.random());
  	  const escapedInput = utils.escapeRegexCharacters(input.trim());
  	  const lowercasedInput = input.trim().toLowerCase();
  	  const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
  	  const suggestions = this.state.productos
  	    .filter( suburbObj => suburbMatchRegex.test(suburbObj.description + ' Marca: ' + suburbObj.brand  + ' Codigo: ' + suburbObj.code) )
  	    .sort( (suburbObj1, suburbObj2) =>
  	      suburbObj1.description.toLowerCase().indexOf(lowercasedInput) -
  	      suburbObj2.description.toLowerCase().indexOf(lowercasedInput)
  	    )
  	    .slice(0, 7)
  	    .map( suburbObj => {
  	      suburbObj.population = suburbObj.qty;
  	      return suburbObj;
  	    } )
  	    .sort( (suburbObj1, suburbObj2) => suburbObj2.population - suburbObj1.population );
  	  setTimeout(() => callback(null, suggestions), requestDelay);
  	}

  	renderSuggestion(suggestionObj, input) {
  	  const escapedInput = utils.escapeRegexCharacters(input);
  	  const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
  	  const suggestion = 'Descripcion: ' + suggestionObj.description + ' /*/ Marca: ' + suggestionObj.brand + ' /*/ Cod.: ' + suggestionObj.code;
  	  const firstMatchIndex = suggestion.search(suburbMatchRegex);

  	  if (firstMatchIndex === -1) {
  	    return suggestion;
  	  }

  	  const beforeMatch = suggestion.slice(0, firstMatchIndex);
  	  const match = suggestion.slice(firstMatchIndex, firstMatchIndex + input.length);
  	  const afterMatch = suggestion.slice(firstMatchIndex + input.length);

  	  return (
  	    <span>
  	      {beforeMatch}<strong>{match}</strong>{afterMatch}<br />
  	      <small style={{ color: '#777' }}>Cantidad: {suggestionObj.population}</small>
  	    </span>
  	  );
  	}

  	getSuggestionValue(suggestionObj) {
  	  var pp = Number(suggestionObj.price)
  	  var pproduct = []
  	  var mproduct = []
  	  var nproduct = []
  	  var qty = Number(suggestionObj.population)
  	  pproduct.push(suggestionObj.code, suggestionObj.description, suggestionObj.brand)
  	  mproduct.push(suggestionObj.description)
  	  nproduct.push(suggestionObj.code)
  	  this.setState({ pPrice: pp, productSale: pproduct, qty: qty, prods: mproduct, prods_code: nproduct})
  	  //return suggestionObj.code + ' - ' + suggestionObj.description + ' - ' + suggestionObj.brand;
  	  return suggestionObj.code;
  	}

	render(){
		return <div className="separador">
			<div className="field_shop">
          		<label ClassName="field-label" for="codeField">Código o Descripción: </label>
          		<Autosuggest suggestions={this.getSuggestions.bind(this)} suggestionRenderer={this.renderSuggestion.bind(this)} suggestionValue={this.getSuggestionValue.bind(this)} inputAttributes={{ id: 'codeField' }} />
          	</div>
			<DescriptionComp  prod={this.state.prods} />
		</div>
	}
}