document.addEventListener('DOMContentLoaded', function() {
    // Functionality for handling answer button clicks
    const buttons = document.querySelectorAll('.answer-button'); // Select all answer buttons
    const hiddenInput = document.getElementById('selected-answer'); // Hidden input to store selected answer
    const form = document.querySelector('form'); // The form element for submission

    // Attach click event listeners to all answer buttons
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove the 'active' class from all buttons to ensure only one is highlighted
            buttons.forEach(btn => btn.classList.remove('active'));

            // Add the 'active' class to the clicked button to visually indicate selection
            this.classList.add('active');

            // Update the value of the hidden input with the value of the selected answer button
            hiddenInput.value = this.getAttribute('data-value');
        });
    });

    // Prevent form submission if no answer is selected
    form.addEventListener('submit', function(event) {
        // Check if the hidden input is empty, meaning no answer was selected
        if (hiddenInput.value === '') {
            event.preventDefault(); // Stop form submission
            alert('Please select an answer before submitting.'); // Alert the user to select an answer
        }
    });

    // Functionality for delete confirmation
    const deleteForms = document.querySelectorAll('.delete-form'); // Select all forms intended for deletion confirmation

    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Display a confirmation dialog before proceeding with form submission
            if (!confirm('Are you sure you want to delete this quiz?')) {
                event.preventDefault(); // Stop form submission if user cancels
            }
        });
    });

    // Functionality for generating and copying the quiz link
    const generateLinkButtons = document.querySelectorAll('.generate-link'); // Select all buttons for generating quiz links
    const linkModal = document.getElementById('linkModal'); // Modal element for displaying the link
    const quizLinkInput = document.getElementById('quiz-link'); // Input field for displaying the quiz link
    const copyLinkButton = document.getElementById('copy-link'); // Button for copying the quiz link

    // Ensure the modal and buttons exist before attaching event listeners
    if (linkModal) {
        generateLinkButtons.forEach(button => {
            button.addEventListener('click', function() {
                const quizId = this.getAttribute('data-quiz-id'); // Get the quiz ID from the button's data attribute
                const link = `${window.location.origin}/quiz/${quizId}/`;  // Generate the quiz link URL
                quizLinkInput.value = link; // Set the generated link as the value of the input field
            });
        });
    }

    // Add event listener to copy the link to clipboard
    if (copyLinkButton) {
        copyLinkButton.addEventListener('click', function() {
            quizLinkInput.select(); // Select the content of the input field
            document.execCommand('copy'); // Copy the selected content to the clipboard
            alert('Link copied to clipboard!'); // Notify the user that the link was copied
        });
    }
});