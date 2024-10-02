#start
print('Initialize Unit Converter')

#convert inches to cm
inches = input('Input inches to be converted to cm: ')
inches = int(inches)
cm = inches * 2.54
print(cm, 'cm')

#convert lbs to kg
pounds = input('Input lbs to be converted to kg: ')
pounds = int(pounds)
kg = pounds / 2.2
print(kg, 'kg')

#convert fahrenheit to celcius
fahrenheit = input('Input fahrenheit to be converted to celcius: ')
fahrenheit = int(fahrenheit)
celcius = (fahrenheit - 32) * (5/9)
print(celcius, 'celcius')

#closing
print('Converter shutting down...')