/*
 * Modules Dependiencies
 */

import React from 'react';
import FormTitulo from './FormTitulo';
import FormClient from './FormClient';

export default class FormMain extends React.Component {
	render(){
		return <form className="form">
		<FormTitulo/>
		<FormClient />
		</form>
	}
}