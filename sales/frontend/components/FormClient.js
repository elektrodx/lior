/*
 * Modules Dependiencies
 */

import React from 'react';
import ReactIntl from 'react-intl';
import FormStock from './FormStock';

var IntlMixin     = ReactIntl.IntlMixin;
var FormattedDate = ReactIntl.FormattedDate;

export default class FormClient extends React.Component{
	mixins: [IntlMixin]
	render(){
		var hoy = Date.now();
		return <div className="form-client">
			<div>
				<label for="ClientName">Nombre: </label>
	          	<input type="text" className="form-control" id="ClientName" placeholder="Introduzca el Nombre del Cliente"/>
          	</div>
          	<div>
          		<label for="ClientCI">CI/NIT:</label>
          		<input type="text" id="ClientCI" placeholder="Introduzca en CI o NIT"/>
          	</div>
          	<div>
          		<FormattedDate locales="es-AR" value={hoy} day="numeric" month="short" year="numeric"/>
          	</div>
          	<FormStock/>
		</div>
	}
}