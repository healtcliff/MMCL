function calculateRemaining() {
    // Get input values
    var tuitionFee = parseFloat(document.getElementById('tuitionFee').value);
    var initialPayment = parseFloat(document.getElementById('initialPayment').value);

    // Check if the input values are valid
    if (isNaN(tuitionFee) || isNaN(initialPayment)) {
        alert('Please enter valid numbers for tuition fee and initial payment.');
        return;
    }

    // Calculate remaining amount
    var remainingAmount = tuitionFee - initialPayment;

    // Update the remaining amount on the page
    document.getElementById('remainingAmount').textContent = remainingAmount.toFixed(2);
}
