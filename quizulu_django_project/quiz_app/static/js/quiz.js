document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.answer-button');
    const submitButton = document.querySelector('.btn-primary');
    
    let selectedAnswer = null;
    
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove 'selected' class from all buttons
            buttons.forEach(btn => btn.classList.remove('selected'));
            
            // Add 'selected' class to the clicked button
            this.classList.add('selected');
            
            // Store the selected answer
            selectedAnswer = this.getAttribute('data-value');
        });
    });
    
    // Ensure selected answer is sent with form submission
    document.querySelector('form').addEventListener('submit', function(event) {
        if (!selectedAnswer) {
            event.preventDefault();
            alert('Please select an answer.');
        } else {
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = 'answer';
            input.value = selectedAnswer;
            this.appendChild(input);
        }
    });
});