document.addEventListener("DOMContentLoaded", function() {
    const correctAnswers = JSON.parse(document.getElementById('correct-answers').textContent);

    function checkAnswer(index) {
        const inputField = document.getElementById(`answer-${index}`);
        const userAnswer = inputField.value.trim().toLowerCase();
        const correctAnswer = correctAnswers[index].trim().toLowerCase();

        if (userAnswer === correctAnswer) {
            inputField.classList.remove("incorrect");
            inputField.classList.add("correct");
            // Отправка статистики на сервер
            fetch(`/update_score`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ correct: true })
            });
        } else {
            inputField.classList.remove("correct");
            inputField.classList.add("incorrect");
        }
    }

    // Привязка обработчиков событий к кнопкам
    const buttons = document.querySelectorAll('.submit-button');
    buttons.forEach((button, index) => {
        button.addEventListener('click', () => checkAnswer(index));
    });
});