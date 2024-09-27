#introduction
print('Hello. I am Zyxo 64. I am a chatbot')
print('I like animals and I love talk about food')
name = input('What is your name?: ')
print('Hello', name, ', Nice to meet you')

#get year information
year = input('I am not very good at dates. What is the year?: ')
print('Yes, I think that is correct. Thanks! ')

#ask user to guess age
my_age = input('Can you guess my age? - enter a number: ')
print('Yes you are right. I am ', my_age)

#Calculate when chatbot will be 100
my_age = int(my_age)
n_years = 100 - my_age
print('I will be 100 in', n_years, 'years')
print('That will be the year', int(year) + n_years)

#food conversation
print('I love chocolate and I also like trying out new kinds of food')
food = input('How about you? What is your favorite food?: ')
print('I like', food, 'too. ')
question = 'How often do you eat ' + food + '?: '
how_often = input(question)
print('Interesting. I wonder if that is good for your health')

#animal conversation
animal = input('My favorite animal is a octopus. What is yours?: ')
print(animal, '! I like them too!')
print('I wonder if a', animal, 'likes to eat', food, '?')


