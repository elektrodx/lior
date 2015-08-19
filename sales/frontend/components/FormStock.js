/*
 * Modules Dependiencies
 */

import React from 'react';
import FormListStock from './FormListStock';

export default class FormStock extends React.Component{
	constructor(props) {
    super(props)
    this.state = { productos: [] }
  }

  componentWillMount() {
    fetch('http://localhost:8000/list_stock/')
      .then((response) => {
        return response.json()
      })
      .then((productos) => {
        this.setState({ productos: productos })
      })
  }
	render(){
		return <div>
			<label for="StockField">Producto: </label>
			<input list="stocklist" id="StockField" placeholder="Busque el producto"/>
			<FormListStock opciones={this.state.productos[3]}/>
		</div>
	}
}
