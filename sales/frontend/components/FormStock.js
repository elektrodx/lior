/*
 * Modules Dependiencies
 */

import React from 'react';
import Autosuggest from 'react-autosuggest';
import utils from './../node_modules/react-autosuggest/examples/src/utils.js';
import PriceField from './PriceField'
//import FormAutoStock from './FormAutoStock';

export default class FormStock extends React.Component{
	constructor(props) {
    super(props)
    this.state = { productos: [], pPrice: 0, productSale: [], qty: 0, qtyf:0, pPricef: 0, parts: 0}
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
    //const suggestions = suburbs
    const suggestions = this.state.productos
      .filter( suburbObj => suburbMatchRegex.test(suburbObj.description + ' Marca: ' + suburbObj.brand  + ' Codigo: ' + suburbObj.code) )
      .sort( (suburbObj1, suburbObj2) =>
        suburbObj1.description.toLowerCase().indexOf(lowercasedInput) -
        suburbObj2.description.toLowerCase().indexOf(lowercasedInput)
      )
      .slice(0, 7)
      .map( suburbObj => {
        //suburbObj.population = population(suburbObj);
        suburbObj.population = suburbObj.qty;
        return suburbObj;
      } )
      .sort( (suburbObj1, suburbObj2) => suburbObj2.population - suburbObj1.population );

    // 'suggestions' will be an array of objects, e.g.:
    //   [{ suburb: 'Mordialloc', postcode: '3195', population: 6943 },
    //    { suburb: 'Mentone', postcode: '3194', population: 5639 },
    //    { suburb: 'Mill Park', postcode: '3082', population: 3631 }]

    setTimeout(() => callback(null, suggestions), requestDelay);
  }

  // function renderSuggestion(suggestion, input) { // In this example, 'suggestion' is a string 
  //   return (                                     // and it returns a ReactElement 
  //     <span><strong>{suggestion.slice(0, input.length)}</strong>{suggestion.slice(input.length)}</span>
  //   );
  // }

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
        <small style={{ color: '#777' }}> Fraccionado: {suggestionObj.parts_left}</small>
        <small style={{ color: '#777' }}> de {suggestionObj.parts}</small>
      </span>
    );
  }

  getSuggestionValue(suggestionObj) {
    if (suggestionObj.parts>0){
      var ppf = Number(suggestionObj.price/suggestionObj.parts)  
    }
    var pp = Number(suggestionObj.price)
    var parts = Number(suggestionObj.parts)
    var pproduct = []
    var qty = Number(suggestionObj.population)
    var qtyf = Number(suggestionObj.parts_left)
    pproduct.push(suggestionObj.code, suggestionObj.description, suggestionObj.brand)
    this.setState({ pPrice: pp, productSale: pproduct, qty: qty, qtyf: qtyf, pPricef: ppf, parts: parts})
    return suggestionObj.code + ' - ' + suggestionObj.description + ' - ' + suggestionObj.brand;
  }

	render(){
		return <div className="form-client-stock">
			<label for="StockField">Producto: </label>
      <span className="field_auto">
        <Autosuggest suggestions={this.getSuggestions.bind(this)} suggestionRenderer={this.renderSuggestion.bind(this)} suggestionValue={this.getSuggestionValue.bind(this)} />
      </span>
      <PriceField price_base={this.state.pPrice} productSold={this.state.productSale} qtyp={this.state.qty} price_basef={this.state.pPricef} parts_left={this.state.qtyf} parts={this.state.parts} />
		</div>
	}
}
