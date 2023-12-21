function validateForm() {
    var qty1 = document.getElementById("qty1").value;
    var qty2 = document.getElementById("qty2").value;
    var town = document.getElementById("town").value;
    var status = document.getElementById("status").value;
    var gender = document.getElementById("gender").value;
    var email = document.getElementById("email").value;
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastname").value;
    var address = document.getElementById("address").value;

    if (qty1 == "" || qty2 == "" || town == "" || status == "" || gender == "" || email == "" || firstName == "" || lastName == "" || address == "") {
        alert("All fields must be filled out");
        return false;
    }

    // Additional validation logic can be added here

    alert("Registration has been submitted");
    return true;
}

function calculateValue() {
    var qty1 = +document.getElementById("qty1").value;
    var qty2 = +document.getElementById("qty2").value;

    document.getElementById("partnerForum").value = 135 * qty1;
    document.getElementById("policySeries").value = 128 * qty2;
    document.getElementById("totalValue").value = (135 * qty1) + (128 * qty2);

    // Additional calculation logic can be added here
}
