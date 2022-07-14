function submitForm(event) {
	// Stop non ajax post
	event.preventDefault();	

	// Get field entries
	form = document.getElementById("form");
	var formData = new FormData(form);
	
	// Send dat via ajax request
	jQuery.ajax({
		url: 'http://localhost:8080',
	    	data: formData,
	    	cache: false,
	    	contentType: false,
	    	processData: false,
	    	method: 'POST',
	    	success: function(data){
			form.reset();
	        	alert(data);
	    	}
	});
}
