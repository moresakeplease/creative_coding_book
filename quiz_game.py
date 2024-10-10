import time

score = 0

questions = ['What is the largest state by Area?', 
             'What mountain range runs along the eastern coast of the United States?',
             'Which U.S. state has the most national parks?',
             'What is the national flower of the United States?',
             'What year did the United States declare independence?',
             'What is the largest city in the United States by population?',
             'What is the only U.S. state that grows coffee commercially?',
             'What natural disaster is the U.S. known for experiencing the most frequently?',
             'Which U.S. president is known for the Emancipation Proclamation?',
             'Which U.S. state was an independent republic before joining the Union?']

answers = ['Alaska',
           'Appalachian Mountains',
           'California',
           'Rose',
           '1776',
           'New York',
           'Hawaii',
           'Tornadoes',
           'Abraham Lincoln',
           'Texas']
#Starting

print('Welcome to the United states Trivia game')
print('****************************************')
time.sleep(2)

for i in range(len(questions)):
        print(questions[i]) 
        user_input = input('Your answer is: ')
        if user_input == answers[i].lower():
            print('Correct!')
            score += 1
        else:
            print('Incorrect')
            print('The answer is', answers[i])

print('Your score is:', score)
if score > 7:
     print('Wow you know your stuff!')
elif score >= 5:
     print('Good try!')
else:
     print('Good Job I hope you learned some new things!')
print()