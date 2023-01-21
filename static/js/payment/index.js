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
