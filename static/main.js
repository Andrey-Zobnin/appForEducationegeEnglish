$(document).ready(function() {
    // Получаем правильные ответы из HTML атрибута данных
    const correctAnswers = JSON.parse($('#taskData').attr('data-answers'));

    // Обработчик для кнопки "Отправить" для каждого поля ввода
    $('.submit-button').on('click', function() {
        const inputField = $(this).siblings('.answer');
        const userAnswer = inputField.val().trim().toUpperCase();
        const index = $(this).parent().index(); // Получаем индекс вопроса

        if (userAnswer === correctAnswers[index]) {
            inputField.removeClass('incorrect').addClass('correct');
        } else {
            inputField.removeClass('correct').addClass('incorrect');
        }
    });

    // Обработчик для кнопки "Проверить все ответы"
    $('#checkAnswers').on('click', function() {
        let score = 0;
        let feedback = [];

        $('.answer').each(function(index) {
            const userAnswer = $(this).val().trim().toUpperCase();
            if (userAnswer === correctAnswers[index]) {
                score++;
                feedback.push(`Вопрос ${index + 1}: Верно!`);
            } else {
                feedback.push(`Вопрос ${index + 1}: Неверно! Правильный ответ: ${correctAnswers[index]}`);
            }
        });

        // Отображаем результат
        $('#result').html(`<p>Вы набрали ${score} из ${correctAnswers.length} правильных ответов!</p><ul>${feedback.map(item => `<li>${item}</li>`).join('')}</ul>`);
    });
});