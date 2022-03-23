$(document).ready(function(){
	
	$('#index-necklace-btn').click(function(){
		window.location.href="{% url 'floppa:necklaces' %}";
	});
});


