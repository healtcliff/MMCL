function calculateRemaining() {
    // Get input values
    var tuitionFee = parseFloat(document.getElementById('tuitionFee').value);
    var initialPayment = parseFloat(document.getElementById('initialPayment').value);

    // Check if the input values are valid positive numbers
    if (isNaN(tuitionFee) || isNaN(initialPayment) || tuitionFee <= 0 || initialPayment <= 0) {
        alert('Please enter valid numbers for tuition fee and initial payment.');
        return;
    }

    // Check if the initial payment is greater than the tuition fee
    if (initialPayment >= tuitionFee) {
        alert('Initial payment exceed the tuition fee.');
        return;
    }

    // Calculate remaining amount
    var remainingAmount = tuitionFee - initialPayment;

    // Update the remaining amount on the page
    document.getElementById('remainingAmount').textContent = remainingAmount.toFixed(2);
}
