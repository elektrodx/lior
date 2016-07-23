/*
 * Modules Dependiencies
 */

import React from 'react';
import Autosuggest from 'react-autosuggest';
import utils from './../node_modules/react-autosuggest/examples/src/utils.js';
import ReactIntl from 'react-intl';
import FormStock from './FormStock';

var IntlMixin     = ReactIntl.IntlMixin;
var FormattedDate = ReactIntl.FormattedDate;

export default class FormClient extends React.Component{
	constructor(props) {
		super(props)
		this.state = { clientes: [], }
		const suburbs_cust = [];
	}

	componentWillMount() {
		fetch('http://127.0.0.1:8000/list_customer/')
		.then((response) => {
			return response.json()
		})
		.then((clientes) => {
			this.setState({ clientes: clientes })
		})
	}

	mixins: [IntlMixin]

	population(suburbObj) {
		return suburbObj.ci.split('').reduce((result, char) => result + char.charCodeAt(0), 0) +
		+suburbObj.name.split('').reverse().join('');
	}

	getSuggestions(input, callback) {
		const requestDelay = 50 + Math.floor(300 * Math.random());
		const escapedInput = utils.escapeRegexCharacters(input.trim());
		const lowercasedInput = input.trim().toLowerCase();
		const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
    	const suggestions = this.state.clientes
    	.filter( suburbObj => suburbMatchRegex.test(suburbObj.ci + ' Nombre: ' + suburbObj.name ) )
    	.sort( (suburbObj1, suburbObj2) =>
    		suburbObj1.ci.toLowerCase().indexOf(lowercasedInput) -
    		suburbObj2.ci.toLowerCase().indexOf(lowercasedInput)
    	)
    	.slice(0, 7)
    	.map( suburbObj => {
        	suburbObj.population = suburbObj.fono;
        	return suburbObj;
    	} )
    	.sort( (suburbObj1, suburbObj2) => suburbObj2.population - suburbObj1.population );
    	setTimeout(() => callback(null, suggestions), requestDelay);
	}

	renderSuggestion(suggestionObj, input) {
		const escapedInput = utils.escapeRegexCharacters(input);
	  	const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
	  	const suggestion = 'CI/NIT: ' + suggestionObj.ci + ' /*/ Nombre: ' + suggestionObj.name;
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
	  		<small style={{ color: '#777' }}>Teléfono: {suggestionObj.population}</small>
	  		</span>
	  		);
	}

	getSuggestionValue(suggestionObj) {
	  	var cclient = []
	  	cclient.push(suggestionObj.ci, suggestionObj.nombre, suggestionObj.fono)
	  	this.setState({ clientSale: cclient } )
	  	document.getElementById("ClientCI").value = suggestionObj.ci;
	  	document.getElementById("ClientName").value = suggestionObj.name;
	  	//return suggestionObj.ci;
	}

	id_to_windowname(text) {
	    text = text.replace(/\./g, '__dot__');
	    text = text.replace(/\-/g, '__dash__');
	    return text;
	}

	showRelatedObjectPopup(triggeringLink) {
		var name = triggeringLink.id;
		name = this.id_to_windowname.bind(name);
		var href = triggeringLink.href;
		var win = window.open('/add_customer', name, 'height=500,width=800,resizable=yes,scrollbars=yes');
		win.focus();
		return false;
	}

	reloadMyDivSales() {
		window.location.reload();
	}

	render(){
		var hoy = Date.now();
		return <div className="form-client">
          	<div className="form-search">
          		<label ClassName="field-label" for="SearchClient">Buscar Cliente por Nombre o CI/NIT:</label>
          		<Autosuggest suggestions={this.getSuggestions.bind(this)} suggestionRenderer={this.renderSuggestion.bind(this)} suggestionValue={this.getSuggestionValue.bind(this)} />
          	    <span id="span_customer">
          	    	<a href="/add_customer" className="add-another" id="add_id_customer" onClick={this.showRelatedObjectPopup.bind(this)}> <img src="../static/admin/img/icon_addlink.gif" width="10" height="10" /> </a>
          		</span>	
          	</div>
          	<br/><br/><br/>
			<div className="form-client-nombre">
				<label for="ClientName">Nombre: </label>
	          	<input type="text" className="form-control" id="ClientName"/>
          	</div>
          	<div className="form-client-ci">
          		<label for="ClientCI">CI/NIT:</label>
          		<input type="text" className="form-control" id="ClientCI"/>
          	</div>
          	<div className="form-client-date">
          		<FormattedDate locales="es-AR" value={hoy} day="numeric" month="numeric" year="numeric"/>
          	</div>
          	<FormStock/>
		</div>
	}
}