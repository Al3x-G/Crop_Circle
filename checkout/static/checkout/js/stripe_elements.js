/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);  // Get value, remove quotes
var clientSecret = $('#id_client_secret').text().slice(1, -1);  // Get value, remove quotes

// Initialise Stripe with the public key
var stripe = Stripe(stripePublicKey);

// Create an instance of Elements
var elements = stripe.elements();

// Stripe styling
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

// Handle realtime validation errors on the card element
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

// Add an event listener to the form for when it is submitted
form.addEventListener('submit', function(ev) {
    ev.preventDefault();  // Prevent the default form submission behavior

    // Disable the card element to prevent further updates while processing the payment
    card.update({ 'disabled': true });

    // Disable the submit button to prevent multiple submissions
    $('#submit-button').attr('disabled', true);

    // Toggle the visibility of the payment form with a fade animation over 100 milliseconds.
    $('#payment-form').fadeToggle(100);

    // Toggle the visibility of the loading overlay with a fade animation over 100 milliseconds.
    $('#loading-overlay').fadeToggle(100);

    // Use Stripe to confirm the card payment with the client secret
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,  // Pass the card element to Stripe
        }
    }).then(function(result) {
        // If there was an error during payment confirmation, display the error message
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            
            // Build HTML to display the error icon and message
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;

            // Display the error message in the 'card-errors' div
            $(errorDiv).html(html);

            // Toggle the visibility of the payment form with a fade animation over 100 milliseconds.
            $('#payment-form').fadeToggle(100);

            // Toggle the visibility of the loading overlay with a fade animation over 100 milliseconds.
            $('#loading-overlay').fadeToggle(100);

            // Re-enable the card input and submit button for retrying the payment
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            // If the payment was successful, check if the payment intent status is 'succeeded'
            if (result.paymentIntent.status === 'succeeded') {
                // If payment was successful, submit the form to finalize the process
                form.submit();
            }
        }
    });
});