document.addEventListener('DOMContentLoaded', function() {
    // Functionality for answer buttons
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

   // Functionality for delete confirmation
   const deleteForms = document.querySelectorAll('.delete-form');

   deleteForms.forEach(form => {
       form.addEventListener('submit', function(event) {
           if (!confirm('Are you sure you want to delete this quiz?')) {
               event.preventDefault(); // Stop form submission if user cancels
           }
       });
   });

     // Functionality for generating and copying quiz link
     const generateLinkButtons = document.querySelectorAll('.generate-link');
     const linkModal = document.getElementById('linkModal');
     const quizLinkInput = document.getElementById('quiz-link');
     const copyLinkButton = document.getElementById('copy-link');
 
     if (linkModal) {
         generateLinkButtons.forEach(button => {
             button.addEventListener('click', function() {
                 const quizId = this.getAttribute('data-quiz-id');
                 const link = `${window.location.origin}/quiz/${quizId}/`;  // Adjust URL format as needed
                 quizLinkInput.value = link;
             });
         });
     }
 
     if (copyLinkButton) {
         copyLinkButton.addEventListener('click', function() {
             quizLinkInput.select();
             document.execCommand('copy');
             alert('Link copied to clipboard!');
         });
     }
});