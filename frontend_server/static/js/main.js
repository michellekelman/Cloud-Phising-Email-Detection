window.onload=function(){
	$('#email_form').submit(function(event){
		event.preventDefault();
		var postData = $(this).serializeArray();
	    var formURL = $(this).attr("action");
	    $.ajax(
	    {
	        url : formURL,
	        type: "POST",
	        data : postData,
	        success:function(data, textStatus, jqXHR) 
	        {
	        	if (data=="Spam"){
	        		$('#ham_alert').hide();
	        		$('#spam_alert').show();
	        	}else{
	        		$('#spam_alert').hide();
	        		$('#ham_alert').show();
	        	}
	        },
	        error: function(jqXHR, textStatus, errorThrown) 
	        {
	            
	        }
	    });
	})
}