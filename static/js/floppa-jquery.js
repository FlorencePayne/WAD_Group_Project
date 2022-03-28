$(document).ready(function() {
    $('#add_to_cart_form').click(function() {
        alert('Please log in to add items to cart'); 
    });
    
    $("#search_input").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#necklaces_table tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});