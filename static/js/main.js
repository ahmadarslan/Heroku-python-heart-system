$(function() {

	'use strict';

	// Form

	var predictForm = function() {

		if ($('#predictForm').length > 0 ) {
			$( "#predictForm" ).validate( {
				rules: {
					age: {
					required:true,
					min:20,
					max:90
					},
					bp: {
						required: true,
					min:50,
					max:200
					},
					chol: {
						required: true,
					min:50,
					max:300
					},
					
				},
				messages: {
					age: {required:"Please enter your age",
					min:"Min age 20 years",
					max:"Max age 90 years"
					},
					bp: "Please enter your blood presure (between 80-200)",
					chol: "Please enter your cholesterol (between 80-300)",
				},
				
				
			});
		}
	};
	predictForm();

});