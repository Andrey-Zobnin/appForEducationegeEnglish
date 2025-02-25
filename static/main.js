// main.js

$(document).ready(function() {
    // Get the correct answers from the HTML data attribute
    const correctAnswers = JSON.parse($('#taskData').attr('data-answers'));

    $('#checkAnswers').on('click', function() 
    {
        
        // massive for loop to iterate over each question and input field
        
        let userAnswers = [];

        // Collect user answers from input fields
        $('.answer').each(function() {
            userAnswers.push($(this).val().trim().toUpperCase());
        });
         
        // Check answers score and for user answers feedback
        let score = 0;
        let feedback = [];

        userAnswers.forEach((answer, index) => {
            if (answer === correctAnswers[index]) {
                score++;
                feedback.push(`Question ${index + 1}: Correct!`);
            } else {
                feedback.push(`Question ${index + 1}: Incorrect! Correct answer: ${correctAnswers[index]}`);
            }
        });

        // Display result
        $('#result').html(`<p>You got ${score} out of ${correctAnswers.length} correct!</p><ul>${feedback.map(item => `<li>${item}</li>`).join('')}</ul>`);
    });
});