// Generate a random ticket number
function generateTicketNumber() {
    return Math.floor(Math.random() * 1000000);
}

// Populate the ticket number in the HTML
document.getElementById('ticket-number').textContent = generateTicketNumber();
