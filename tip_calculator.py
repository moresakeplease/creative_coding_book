#start
print('Initialize tip calculator...')
bill = input('What is the total amount on the bill?: ')
percent = input('What is the percentage you would like to tip today?: ')
party = input('How many people will be sharing this bill?: ')
bill = int(bill)
percent = int(percent)
party = int(party)
print('----------------------')

#calulations
tip = bill * (percent/100)
print('Tip amount = ', tip)
print('Total bill = ', bill)
print('----------------------')

#totals
tip_per = tip / party
bill_per = bill / party
print('Tip amount per person = ', tip_per)
print('Total bill per person = ', bill_per)
print('----------------------')

#closing
print('Thankyou for using the tip calculator, Goodbye')