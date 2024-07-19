document.addEventListener("DOMContentLoaded", function() {
    // Select the input field by its name attribute
    var usernameInput = document.querySelector('input[name="username"]');
    
    // Set the placeholder attribute
    if (usernameInput) {
        usernameInput.placeholder = "Username";
    }
});
