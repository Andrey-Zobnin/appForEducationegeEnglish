// main.js

$(document).ready(function() {
    $('#checkAnswers').on('click', function() {
        let correctAnswers = ["FAMOUS", "UNHAPPY"]; // Example correct answers
        let userAnswers = [];

        // Collect user answers from input fields
        $('.answer').each(function(index) {
            userAnswers.push($(this).val().trim().toUpperCase());
        });

        // Check answers
        let score = 0;
        userAnswers.forEach((answer, index) => {
            if (answer === correctAnswers[index]) {
                score++;
            }
        });

        // Display result
        $('#result').text(`You got ${score} out of ${correctAnswers.length} correct!`);
    });
});