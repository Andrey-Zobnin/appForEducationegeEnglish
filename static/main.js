$(document).ready(function() {
    // Get the correct answers from the HTML data attribute
    const correctAnswers = JSON.parse($('#taskData').attr('data-answers'));

    $('#checkAnswers').on('click', function() {
        // Array to collect user answers
        let userAnswers = [];

        // Collect user answers from input fields
        $('.answer').each(function() {
            userAnswers.push($(this).val().trim().toUpperCase());
        });
         
        // Check answers score and provide user feedback
        let score = 0;
        let feedback = [];

        userAnswers.forEach((answer, index) => {
            if (answer === correctAnswers[index]) {
                score++;
                feedback.push(`Вопрос ${index + 1}: Верно!`);
            } else {
                feedback.push(`Вопрос ${index + 1}: Неверно! Правильный ответ: ${correctAnswers[index]}`);
            }
        });

        // Display result
        $('#result').html(`<p>Вы набрали ${score} из ${correctAnswers.length} правильных ответов!</p><ul>${feedback.map(item => `<li>${item}</li>`).join('')}</ul>`);
    });
});