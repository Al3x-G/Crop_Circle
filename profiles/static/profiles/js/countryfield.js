// Get the initial value of the #id_default_country dropdown
let countrySelected = $('#id_default_country').val();

// If no country is selected (value is empty), set the text color to grey (#aab7c4)
if (!countrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}

// Add an event listener for changes to the #id_default_country dropdown
$('#id_default_country').change(function() {
    // Update the countrySelected variable with the new value
    countrySelected = $(this).val();

    // Check if the new value is empty
    if (!countrySelected) {
        // If no country is selected, set the text color to grey (#aab7c4)
        $(this).css('color', '#aab7c4');
    } else {
        // If a country is selected, set the text color to black (#000)
        $(this).css('color', '#000');
    }
});