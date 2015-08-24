/*
 * Modules Dependiencies
 */

import React from 'react';
import Autosuggest from 'react-autosuggest';
import utils from './../node_modules/react-autosuggest/examples/src/utils.js';
import suburbs from './../node_modules/react-autosuggest/examples/src/suburbs.json';
 
//const suburbs = ['Cheltenham', 'Mill Park', 'Mordialloc', 'Nunawading'];
 
// function getSuggestions(input, callback) {
//   const regex = new RegExp('^' + input, 'i');
//   const suggestions = suburbs.filter(suburb => regex.test(suburb));
 
//   setTimeout(() => callback(null, suggestions), 300); // Emulate API call 
// }
function population(suburbObj) {
  return suburbObj.suburb.split('').reduce((result, char) => result + char.charCodeAt(0), 0) +
         +suburbObj.postcode.split('').reverse().join('');
}

function getSuggestions(input, callback) {
  const requestDelay = 50 + Math.floor(300 * Math.random());
  const escapedInput = utils.escapeRegexCharacters(input.trim());
  const lowercasedInput = input.trim().toLowerCase();
  const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
  const suggestions = suburbs
    .filter( suburbObj => suburbMatchRegex.test(suburbObj.suburb + ' VIC ' + suburbObj.postcode) )
    .sort( (suburbObj1, suburbObj2) =>
      suburbObj1.suburb.toLowerCase().indexOf(lowercasedInput) -
      suburbObj2.suburb.toLowerCase().indexOf(lowercasedInput)
    )
    .slice(0, 7)
    .map( suburbObj => {
      suburbObj.population = population(suburbObj);
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

function renderSuggestion(suggestionObj, input) {
  const escapedInput = utils.escapeRegexCharacters(input);
  const suburbMatchRegex = new RegExp('\\b' + escapedInput, 'i');
  const suggestion = suggestionObj.suburb + ' VIC ' + suggestionObj.postcode;
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
      <small style={{ color: '#777' }}>Population: {suggestionObj.population}</small>
    </span>
  );
}

function getSuggestionValue(suggestionObj) {
  return suggestionObj.suburb + ' VIC ' + suggestionObj.postcode;
}

export default class FormStock extends React.Component{
	render(){
		return <div>
			<label for="StockField">Producto: </label>
			<Autosuggest suggestions={getSuggestions} suggestionRenderer={renderSuggestion} suggestionValue={getSuggestionValue} />
		</div>
	}
}
