var stripe = Stripe('sk_test_51K7ynJGlpPduiwahiUaCtLBMeDpIIqxVRhugecNbRGmBzFDMuA4khyDmzMM0uUcsjZKRL0mWQhBqCnFB5Wqvg3dF00aVIkritV');

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');
var elements = stripe.elements();

var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px'
    }
};

var card = elements.create("card", { style: style });
card.mount("#card-element");

// for card errors
card.on('change', function (event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
        $('#card-errors').addClass('alert alert-info');
    }
    else {
        displayError.textContent = '';
        $('#card-errors').removeClass('alert alert-info');
    }
});

var form = document.getElementById('payment-fomr');
form.addEventListener('submit', function (e) {
    e.preventDefault();

    var custName = document.getElementById('customer').value;
    var custAdd = document.getElementById('custAdd').value;
    var custAdd2 = document.getElementById('custAdd2').value;
    var postCode = document.getElementById('postCode').value;

    stripe.confirmCardPayment(clientsecret, {
        payment_method: {
            card: card,
            billing_details: {
                address: {
                    line1:custAdd,
                    line2:custAdd2,
                },
                name: custName
            },
        }
    }).then(function (result) {
        if (result.error) {
            console.log('payment error');
            console.log(result.error.message);
            console.log(result.paymentIntent);
        }
        else {
            if (result.paymentIntent.status === 'succeeded') {
                console.log('payment processed')                
                window.location.replace('http://127.0.0.1:88/payment/orderplaced/');
            }
        }
    })
})