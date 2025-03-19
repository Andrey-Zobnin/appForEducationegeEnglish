$(document).ready(function() {
    // Получаем правильные ответы из HTML атрибута данных
    const correctAnswers = JSON.parse($('#taskData').attr('data-answers'));

    // Обработчик для кнопки "Отправить" для каждого поля ввода
    $('.submit-button').on('click', function() {
        const inputField = $(this).siblings('.answer');
        const userAnswer = inputField.val().trim(); // Убираем пробелы по краям
        const index = $(this).parent().index(); // Получаем индекс вопроса

        // Проверка на валидность
        if (userAnswer === "") {
            alert("Пожалуйста, введите ответ."); // Проверка на пустой ввод
            inputField.removeClass('correct incorrect'); // Убираем классы
            return; // Выход из функции
        }

        // Проверяем, что индекс не выходит за пределы массива
        if (index < correctAnswers.length) {
            console.log(`Пользовательский ответ: ${userAnswer}, Правильный ответ: ${correctAnswers[index]}`); // Отладка

            if (userAnswer.toUpperCase() === correctAnswers[index].toUpperCase()) {
                inputField.removeClass('incorrect').addClass('correct');
            } else {
                inputField.removeClass('correct').addClass('incorrect');
            }
        } else {
            console.error("Индекс выходит за пределы массива правильных ответов.");
        }
    });

    // Обработчик для кнопки "Проверить все ответы"
    $('#checkAnswers').on('click', function() {
        let score = 0;
        let feedback = [];

        $('.answer').each(function(index) {
            const userAnswer = $(this).val().trim(); // Убираем пробелы по краям
            console.log(`Проверка ответа ${index + 1}: ${userAnswer}`); // Отладка

            // Проверка на валидность
            if (userAnswer === "") {
                feedback.push(`Вопрос ${index + 1}: Пожалуйста, введите ответ.`);
                $(this).removeClass('correct incorrect'); // Убираем классы
                return; // Выход из функции
            }

            if (userAnswer.toUpperCase() === correctAnswers[index].toUpperCase()) {
                score++;
                feedback.push(`Вопрос ${index + 1}: Верно!`);
                $(this).removeClass('incorrect').addClass('correct'); // Убедитесь, что правильные ответы отмечены
            } else {
                feedback.push(`Вопрос ${index + 1}: Неверно! Правильный ответ: ${correctAnswers[index]}`);
                $(this).removeClass('correct').addClass('incorrect'); // Убедитесь, что неправильные ответы отмечены
            }
        });

        // Отображаем результат
        $('#result').html(`<p>Вы набрали ${score} из ${correctAnswers.length} правильных ответов!</p><ul>${feedback.map(item => `<li>${item}</li>`).join('')}</ul>`);
    });
});