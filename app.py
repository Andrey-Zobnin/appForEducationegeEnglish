from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/task/<int:task_id>')
def task(task_id):
    # Example data for demonstration
    tasks = {
        1: {
            "questions": [
                "Thousands of tourists visit Edinburgh every year. The capital of Scotland is 29______ (FAME) for its history and architecture.",
                "There are pills for everything. If you can't sleep you take a pill. If you're depressed or just 29_____ (HAPPY), you can also take a pill."
            ],
            "answers": ["FAMOUS", "UNHAPPY"]
        },
        2: {
            "questions": [
                "People spend hours talking on their mobile phones. There is an opinion that it may be 29_______ (HARM) to their health.",
                "Learning languages is becoming a popular hobby with children and adults. It’s not only interesting but very 29________ (USE), too."
            ],
            "answers": ["HARMFUL", "USEFUL"]
        },
        3: {
            "questions": [
                "British cuisine is simple. Puddings, stews, pies and breads are 29______ (TRADITION) British dishes.",
                "How do people learn the news? About a century ago people got 29________ (INFORM) from newspapers."
            ],
            "answers": ["TRADITIONAL", "INFORMATION"]
        },
        4: {
            "questions": [
                "Ratatouille is an American cartoon. The name of the cartoon comes from a 29___________ (TRADITION) French dish made of vegetables.",
                "Dublin is the capital city of the Republic of Ireland. It has an 29.__________________ (NATIONAL) airport with flights from London."
            ],
            "answers": ["TRADITIONAL", "INTERNATIONAL"]
        },
        5: {
            "questions": [
                "What do you think is the most stressful and 29. __________________ (DANGER) job in Britain?",
                "My first job was working at a bakery. When I walked from my house to the bakery I could smell the 29. __________________ (WONDER) aroma of the fresh bread."
            ],
            "answers": ["DANGEROUS", "WONDERFUL"]
        },
        6: {
            "questions": [
                "In Andorra people live longer than in any other European country. It seems they have discovered the secret of a long and 29. __________________ (HEALTH) life.",
                "Ballroom dancing in the UK is making a comeback. For the past five years its popularity has grown thanks to the TV show 'Strictly Come Dancing'."
            ],
            "answers": ["HEALTHY", "DANCER"]
        },
        7: {
            "questions": [
                "The best thing about shopping in London is that there really are hundreds of cool shops selling 29. ________________ (FASHION) clothes.",
                "London is famous for its history and its sights. It is also a wonderful place for shopaholics."
            ],
            "answers": ["FASHIONABLE", "FAMOUS"]
        },
        8: {
            "questions": [
                "Every year the world goes dark for one hour, the Earth Hour. The event is organised by the 29. ____________ (NATION) World Wildlife Fund.",
                "The Turners were not used to snow. The most they ever got in Birmingham was an inch or so each winter."
            ],
            "answers": ["INTERNATIONAL", "UNUSUAL"]
        },
        9: {
            "questions": [
                "Dr Michael Werner says that he has eaten nothing for four years. The German 29. ___________ (SCIENCE) explains that he gets all his energy from sunlight.",
                "Many tourists don't like staying in city hotels. They prefer to avoid 29. _____________ (NOISE) cities completely."
            ],
            "answers": ["SCIENTIST", "NOISY"]
        },
        10: {
            "questions": [
                "Piranhas are South American fish. There are lots of scary stories about them. Most people think that piranhas are very 29. __________________ (DANGER) creatures.",
                "Have you heard of a Tadeus Bodnar? He is a 29. ______________ (FAME) Hungarian hairdresser."
            ],
            "answers": ["DANGEROUS", "FAMOUS"]
        },
        11: {
            "questions": [
                "People are afraid of lots of things. There are many 29. __________ (DIFFER) kinds of fears called phobias.",
                "Last spring my best friend Isabelle and I booked a holiday in Venice. We rented a small apartment for a week with a 29. _____________ (WONDER) view of the town."
            ],
            "answers": ["DIFFERENT", "WONDERFUL"]
        },
        12: {
            "questions": [
                "Last year my friend Mia and I went on holiday to Thailand. We stayed in a 29. ___________ (FAME) resort which is popular with tourists.",
                "I unexpectedly met my old friend Natalie at a metro station in Paris. I recognised her at once though we hadn’t seen each other for ten years."
            ],
            "answers": ["FAMOUS", "UNUSUAL"]
        },
        13: {
            "questions": [
                "Jenny doesn’t have many friends, but she has lots of books. Jenny likes fantasy stories best. She has a rich 29. __________ (IMAGINE) which takes her to magical lands.",
                "Sam went to the giant aquarium near his house at least three times a week. He liked the fish and crabs, but the most 29. __________________ (WONDER) creatures there were sharks."
            ],
            "answers": ["IMAGINATION", "WONDERFUL"]
        },
        14: {
            "questions": [
                "It all started in 1865. A group of Frenchmen were having dinner in one of the most 29. _________________ (FASHION) restaurants near Paris.",
                "Father's Day in the UK is on the third Sunday in June. We enjoy this day very much and always arrange a 29. __________ (CELEBRATE) at home."
            ],
            "answers": ["FASHIONABLE", "CELEBRATION"]
        },
        15: {
            "questions": [
                "Olivia got a camera for her birthday. Her family was going on a trip to Washington D.C. and Olivia wanted to take pictures of the 29. __________ (WONDER) places she would see.",
                "The Grand National is a horse race which is held every year in Liverpool. This 29. _________ (COMPETE) involves a four-mile race."
            ],
            "answers": ["WONDERFUL", "COMPETITION"]
        },
        16: {
            "questions": [
                "Last year, I became a volunteer in a charity shop. It was an 29. _________ (USUAL) job for me - I had never been involved with charities.",
                "Lots of companies do business online. They sell goods and services, or provide 29. __________ (INFORM) to the general public."
            ],
            "answers": ["UNUSUAL", "INFORMATION"]
        },
        17: {
            "questions": [
                "If someone asks what your nationality is, how do you answer? For British people 29. _________ (NATION) identity is a complex issue.",
                "The city of St Davids is situated on the south-west coast of Wales. If you're looking for an 29. ___________ (USUAL) place to go, this is your destination."
            ],
            "answers": ["NATIONAL", "UNUSUAL"]
        },
        18: {
            "questions": [
                "Reading is one of the most popular pastimes and books are one of the main sources of knowledge. Everyone knows this but, 29. _______________ (FORTUNATELY), there are many young people who don’t like to read.",
                "Siem Reap is a small town in Cambodia, a country in southeast Asia. It is built around a 29. _____________ (FAME) cathedral."
            ],
            "answers": ["UNFORTUNATELY", "FAMOUS"]
        },
        19: {
            "questions": [
                "The job was not easy but I enjoyed it very much. All my colleagues were very helpful. Their 31. __________ (FRIEND) and support meant a lot to me.",
                "Andrew, my boss and 32. ________ (MANAGE), was a smart and well-organized person."
            ],
            "answers": ["FRIENDLINESS", "MANAGER"]
        },
        20: {
            "questions": [
                "The animals got stronger and healthier without any exercise. However, some doctors think that such pills can be 32________ (DANGER) for health.",
                "The problem is that there will be people who may use the pill unwisely."
            ],
            "answers": ["DANGEROUS", "UNWISE"]
        },
        21: {
            "questions": [
                "The choice of dishes has been influenced by the climate, history and 30_________ (GEOGRAPHY) position of the country.",
                "England is 31______ (FAME) for its butter and cheese."
            ],
            "answers": ["GEOGRAPHICAL", "FAMOUS"]
        },
        22: {
            "questions": [
                "Scotland is known for its 32______ (TASTE) meat dishes and cakes.",
                "Wales has a strong fishing culture. As a result, Welsh cookery includes a lot of seafood."
            ],
            "answers": ["TASTY", "SEAFOOD"]
        },
        23: {
            "questions": [
                "However, nowadays most British restaurants offer food from 33_______ (DIFFER) parts of the world.",
                "The choice depends only on your pocketbook and your 34______ (IMAGINE)."
            ],
            "answers": ["DIFFERENT", "IMAGINATION"]
        },
        24: {
            "questions": [
                "The Internet has changed the situation dramatically. Now the audience has an opportunity to create the news, share their 31_______ (PERSON) knowledge and express their opinions.",
                "The Internet supposes interaction, which makes it very 32________ (ATTRACT) to people."
            ],
            "answers": ["PERSONAL", "ATTRACTIVE"]
        },
        25: {
            "questions": [
                "And what about the newspapers? Will they 33________ (APPEAR) in the near future?",
                "I wish they wouldn’t as I like starting my day with a cup of coffee and a 34______ (TRADITION) newspaper."
            ],
            "answers": ["DISAPPEAR", "TRADITIONAL"]
        },
        26: {
            "questions": [
                "The main character is a rat Remy, who is interested in cooking and dreams of becoming a 30 _____________ (SUCCESS) chef.",
                "Remy is separated from his family at the 31_____________ (BEGIN) of the movie."
            ],
            "answers": ["SUCCESSFUL", "BEGINNING"]
        },
        27: {
            "questions": [
                "So he finds himself in Paris, France. There his unusual 32__________________ (FRIEND) with a poor boy begins.",
                "They both don’t care that most people hate rats and try to get rid of them."
            ],
            "answers": ["FRIENDSHIP", "HATE"]
        },
        28: {
            "questions": [
                "Remy wants to help the boy. He tries to teach him how to cook 33__________________ (TASTE) dishes.",
                "The story ends 34 __________________ (HAPPY) and the friends start a new restaurant."
            ],
            "answers": ["TASTY", "HAPPILY"]
        },
        29: {
            "questions": [
                "Dublin is a green city. It is such a pleasure to walk there on a hot 33. __________________ (SUN) day.",
                "In the evening you can listen to 34. __________________ (TRADITION) Irish music played in the streets and in the pubs."
            ],
            "answers": ["SUNNY", "TRADITIONAL"]
        },
        30: {
            "questions": [
                "What do you think is the most stressful and 29. __________________ (DANGER) job in Britain?",
                "Is it a police officer, a detective or a news 30. __________________ (REPORT)?"
            ],
            "answers": ["DANGEROUS", "REPORTER"]
        },
        31: {
            "questions": [
                "Well, statistics say it is a London taxi driver. It is a 31. __________________ (REAL) hard job as traffic is getting worse.",
                "If we sit in a traffic jam for a few minutes, we start feeling 32. __________________ (NERVE) and irritated."
            ],
            "answers": ["REALLY", "NERVOUS"]
        },
        32: {
            "questions": [
                "But imagine you had to do that every day as your job! And you have to remain 33. __________________ (CARE) and attentive in spite of everything.",
                "London taxi drivers have to have a good memory to be able to take a 34. __________________ (TRAVEL) from A to B without looking at the map."
            ],
            "answers": ["CAREFUL", "TRAVEL"]
        },
        33: {
            "questions": [
                "My first job was working at a bakery. When I walked from my house to the bakery I could smell the 29. __________________ (WONDER) aroma of the fresh bread.",
                "I loved it. I worked 30. ________________ (DAY) after school and at weekends."
            ],
            "answers": ["WONDERFUL", "DAILY"]
        },
        34: {
            "questions": [
                "One of the most 31. __________________ (FANTASY) things about the bakery was that I could eat all I wanted there.",
                "I really couldn't stop eating the fresh buns, rolls and cakes."
            ],
            "answers": ["FANTASTIC", "FRESH"]
        },
        35: {
            "questions": [
                "They were so 32. __________________ (TASTE). Mrs. Bradley, the 33.__________________ (OWN) of the bakery, was a very nice woman.",
                "She had no children and she treated me like her own granddaughter."
            ],
            "answers": ["TASTY", "OWNER"]
        },
        36: {
            "questions": [
                "I liked her too and did my best to be as 34. ___________ (HELP) as possible.",
                "In Andorra people live longer than in any other European country."
            ],
            "answers": ["HELPFUL", "LONGER"]
        },
        37: {
            "questions": [
                "It seems they have discovered the secret of a long and 29. __________________ (HEALTH) life.",
                "People in Andorra stay active and 30. _________________  (ENERGY) at old age."
            ],
            "answers": ["HEALTHY", "ENERGETIC"]
        },
        38: {
            "questions": [
                "They attend gyms and public 31. __________________ (SWIM) pools for free.",
                "Exercise is one reason, the others are clean air and a diet based on vegetables and olive oil."
            ],
            "answers": ["SWIMMING", "CLEAN"]
        },
        39: {
            "questions": [
                "People of all ages in Andorra are cheerful and 32. __________________ (FRIEND).",
                "They think that life is 33. __________________ (FANTASY) and they do their best to enjoy it."
            ],
            "answers": ["FRIENDLY", "FANTASTIC"]
        },
        40: {
            "questions": [
                "Andorra is the most 34. ______________ (PEACE) country in Europe – they haven’t had a war for 700 years.",
                "Ballroom dancing in the UK is making a comeback."
            ],
            "answers": ["PEACEFUL", "DANCING"]
        }
    }
    
    task_data = tasks.get(task_id, {"questions": ["no task"], "answers": []})
    
    return render_template('task.html', task_id=task_id, questions=task_data["questions"], answers=task_data["answers"])

@app.route('/update_score', methods=['POST'])
def update_score():
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)