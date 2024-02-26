# Feb Capstone Project

questions =('How many degrees Celsius is necessary to make water boil?', 
            'What is the capital of Sweden?', 
            'How many countries are in North America?', 
            'How many data types are in Python?')

options = (('A. 68', 'B. 100', 'C. 212'), 
           ('A. Stockholm', 'B. Gothenburg', 'C. Malmö'), 
           ('A. 4', 'B. 7', 'C. 3'),
           ('A. 3', 'B. 5', 'C. 4'))

answers = ('B','A', 'C', 'C' )
user_options = []
score = 0
question_num = 0

for question in questions:
    print()
    print(question)
    for option in options[question_num]:
        print(option)
    
    user_input = input('Enter (A, B, C):').upper()
    user_options.append(user_input)
    if user_input == answers[question_num]:
        score += 1
        print('Correct Answer')
    else:
        print('Incorrect')
        print(f'{answers[question_num]} is the correct answer')
    
    question_num += 1


print(f'Final Result is: {score}')

