/*
 * Modules Dependiencies
 */

import React from 'react';

export default class FormClient extends React.Component{
	var d = new date()
	render(){
		return <div className="form-client">
			<label For="ClientName">Nombre: </label>
          <input type="text" className="form-control" id="ClientName" placeholder="Introduzca el Nombre del Cliente"/>
		</div>
	}
}