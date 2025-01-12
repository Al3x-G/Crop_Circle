/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);  // Get value, remove quotes.
var clientSecret = $('#id_client_secret').text().slice(1, -1);  // Get value, remove quotes.

// Initialise Stripe with the public key.
var stripe = Stripe(stripePublicKey);

// Create an instance of Elements.
var elements = stripe.elements();

// Stripe styling.
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element.
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// This code handles the entire process of submitting a payment form using Stripe Elements.
var form = document.getElementById('payment-form');

// Add an event listener to the form for when it is submitted.
form.addEventListener('submit', function(ev) {
    ev.preventDefault();  // Prevent the default form submission behavior.

    // Disable the card element to prevent further updates while processing the payment.
    card.update({ 'disabled': true });

    // Disable the submit button to prevent multiple submissions.
    $('#submit-button').attr('disabled', true);

    // Toggle the visibility of the payment form with a fade animation over 100 milliseconds.
    $('#payment-form').fadeToggle(100);

    // Toggle the visibility of the loading overlay with a fade animation over 100 milliseconds.
    $('#loading-overlay').fadeToggle(100);

    // Retrieve the 'checked' attribute from the checkbox with id 'id-save-info' and convert it to a boolean (true if checked, false if unchecked).
    var saveInfo = Boolean($('#id-save-info').attr('checked'));

    // Retrieve the CSRF token value from the input field with the name 'csrfmiddlewaretoken' in the form.
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    // Create an object with the necessary data to be sent in the POST request.
    var postData = {
        'csrfmiddlewaretoken': csrfToken,  // Include the CSRF token for security purposes.
        'client_secret': clientSecret,      // Include the client secret for the transaction or payment.
        'save_info': saveInfo,              // Include the value indicating whether the user's information should be saved.
    };

    // Define the URL to which the data will be sent.
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
          // Use Stripe to confirm the card payment with the client secret.
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,  // Pass the card element and billing/shipping details to Stripe. 
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address1.value),
                        line2: $.trim(form.street_address2.value),
                        city: $.trim(form.town_or_city.value),
                        country: $.trim(form.country.value),
                        state: $.trim(form.county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            // If there was an error during payment confirmation, display the error message.
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                
                // Build HTML to display the error icon and message.
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;

                // Display the error message in the 'card-errors' div.
                $(errorDiv).html(html);

                // Toggle the visibility of the payment form with a fade animation over 100 milliseconds.
                $('#payment-form').fadeToggle(100);

                // Toggle the visibility of the loading overlay with a fade animation over 100 milliseconds.
                $('#loading-overlay').fadeToggle(100);

                // Re-enable the card input and submit button for retrying the payment.
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else {
                // If the payment was successful, check if the payment intent status is 'succeeded'.
                if (result.paymentIntent.status === 'succeeded') {
                    // If payment was successful, submit the form to finalize the process.
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // If fails, reload page, error will be in django messeges.
        location.reload();
    })
});