document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.answer-button');
    const hiddenInput = document.getElementById('selected-answer');
    const form = document.querySelector('form');

    // Add click event listeners to all answer buttons
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            buttons.forEach(btn => btn.classList.remove('active'));

            // Add active class to the clicked button
            this.classList.add('active');

            // Set the value of the hidden input to the selected answer
            hiddenInput.value = this.getAttribute('data-value');
        });
    });

    // Prevent form submission if no answer is selected
    form.addEventListener('submit', function(event) {
        if (hiddenInput.value === '') {
            event.preventDefault(); // Stop form submission
            alert('Please select an answer before submitting.');
        }
    });
});