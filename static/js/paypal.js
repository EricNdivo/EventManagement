// Generate a random ticket number
function generateTicketNumber() {
    return Math.floor(Math.random() * 1000000);
}

// Populate the ticket number in the HTML
document.getElementById('ticket-number').textContent = generateTicketNumber();

// Initialize PayPal Button
paypal.Buttons({
    createOrder: function(data, actions) {
        return actions.order.create({
            purchase_units: [{
                amount: {
                    value: '10.00' // Amount for the ticket
                }
            }]
        });
    },
    onApprove: function(data, actions) {
        return actions.order.capture().then(function(details) {
            alert('Transaction completed by ' + details.payer.name.given_name);
            // Here you can display the virtual ticket or redirect to a confirmation page
        });
    }
}).render('#paypal-button-container');
