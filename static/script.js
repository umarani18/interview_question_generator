document.addEventListener('DOMContentLoaded', function() {
    // Get the form element
    const form = document.getElementById('questionForm');
    const generateButton = document.getElementById('generateButton');
    const spinner = document.getElementById('spinner');

    // Add event listener to form submission
    if (form) {
        form.addEventListener('submit', function() {
            // Show loading spinner
            if (spinner) {
                spinner.classList.remove('d-none');
            }
            
            // Disable the button
            if (generateButton) {
                generateButton.disabled = true;
                generateButton.innerText = 'Generating...';
            }
        });
    }
});