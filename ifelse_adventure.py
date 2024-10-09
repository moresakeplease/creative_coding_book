import time

#adventure rpg

print('Welcome to the land of Awwe!')
print('*******************************')
time.sleep(2)
print('You are a brave adventurer seeking the legendary treasure of Awwe.')
print('The treasure is said to be hidden deep within the Whispering Forest.')
time.sleep(2)
print("Armed with your map and a trusty sword, you stand at the forest's edge.")
print('There are two paths you can take.')
time.sleep(2)
print('The left(l) path, known for its beautiful flowers.')
print('Or the right(r) path, rumored to be dark and mysterious.')
time.sleep(2)

#Scenario 1
direction = input('what do you choose?: ')
while not (direction == 'l' or direction == 'r'):
    direction = input('That is an invalid input. Enter l or r: ')

#direction l
if direction == 'l':
    print('You walk down the left path, surrounded by vibrant flowers')
    print('Suddenly, you hear a rustling in the bushes.')
    time.sleep(2)    

#choice 1    
    choice1 = input('Approach Cautiously(a) or Run away(r)?: ')
    while not (choice1 == 'a' or choice1 =='r'):
        choice1 = input('That is an invalid input. Enter a or r: ')
    if choice1 == 'a':
        print('You discover a friendly fairy who offers you a magic potion that grants you protection and healing. And offers to be a guide.')
        print('You continue deeper into the forest, feeling brave.')
        time.sleep(2)
        print('The forest begins to become darker by each passing momment.')
        print('And the fairy that was following you is suddenly not there')
        time.sleep(2)
        choice1_a = input('Do you draw your sword(s) or call out for the fairy(f)?: ')
        while not (choice1_a == 's' or choice1_a == 'f'):
            choice1_a = input('That is an inavlid input. Enter s or f: ')
        if choice1_a == 's':
            print('You decide to draw your sword, prepared for battle.')
            print('You listen closely...')
            time.sleep(2)
            print('A giant spider jumps from the high branches and you stab at the spider coming down at you!')
            print('Another spider comes from behind and once again the spider was not match for you.')
            time.sleep(2)
            choice1_b = input('You remember the potion the fairy gave you. Do you drink it? yes(y) or no?(n): ')
            while not (choice1_b == 'y' or choice1_b == 'n'):
                choice1_b = input('That is an invalid input. Enter y or n: ')
            if choice1_b == 'y':
                print('As the horde of spiders keep coming you decide it would be best to retreat.')
                print('Running through the forest you come across the injured fairy...')
                time.sleep(2)
                print('You could not save the fairy...')
                print('And without a guide you are now lost in the forest')
                time.sleep(2)
                print('Your Journey has come to a end')
                print('Game Over')
            else:
                print('As the horde of spiders keep coming you decide it would be best to retreat.')
                print('Running through the forest you come across the injured fairy...')
                time.sleep(2)
                print('You give the fairy the magic potion you recieved earlier')
                print('The fairy is instantly healed')
                time.sleep(2)
                print('The fairy thanks you')
                print('You are guided out of the forest and have found the treasure of Awwe!')
                time.sleep(2)
                print('Congratulations!')
                print('You have won the game!')
        else:
            print('You call out for the fairy, but no answer')
            print('Unprepared you are ambushed by a giant spider!')
            time.sleep(2)
            print('You have met your fate...')
            time.sleep(2)
            print('Your Journey has come to a end')
            print('Game Over')
            



    else:
        print('You stumble back and trip, losing your map in the process.')
        print('You wander aimlessly.')
        time.sleep(2)
        print('The forest begins to become darker by each passing momment.')
        print('You fall to the ground tired and hungry')
        time.sleep(2)
        print('You have met your fate...')
        time.sleep(2)
        print('Your Journey has come to a end')
        print('Game Over')
    
#Scenario 2
else:
    print('You venture down the right path, where shadows loom and the air is thick with mystery')
    print('You encounter a giant spider blocking your way.')
    time.sleep(2)
    
#choice 2    
    choice2 = input('Do you fight(f) the spider with your sword or do you negotiate(n)?: ')
    while not (choice2 == 'f' or choice2 == 'n'):
        choice2 = input('That is an invalid input. Enter f or n: ')
    if choice2 == 'f':
        print('You bravely fight the spider, but it is too strong.')
        print('You manage to escape but get injured, forcing you to retreat and seek healing.')
        time.sleep(2)
        print('You escaped the dark woods')
        print('You survived')
        time.sleep(2)
        print('But, your Journey has come to a end')
        print('Game Over')

    else:
        print('Surprisingly, the spider understands you and agrees to let you pass in exchange for a shiny object.')
        print('You hand over your compass')
        time.sleep(2)
        print('you continue through the woods, and you hear a faint sound coming from the distance')
        choice2_a = input('Do you follow the sound of the voice? yes(y) or no(n): ')
        while not (choice2_a == 'y' or choice2_a == 'n'):
            choice2_a = input('That is an invalid input. Enter y or n: ')
        if choice2_a == 'y':
            print('You decide to follow the enchanting sound, and come upon a lake')
            print('The water is clear and fresh and the sound of running water calms you')
            time.sleep(2)
            print('You see a women, an elf dressed in a sheer green dress wearing a crown of leaves')
            choice2_b = input('Do you approach the elf? yes(y) or no(n): ')
            while not (choice2_b == 'y' or choice2_b == 'n'):
                choice2_b = input('That is an invalid input. Enter y or n: ')
            if choice2_b == 'y':
                print('You approach the elf, standing behind her as she looks into the waterfall')
                print('She says, "I know why you are here, you are looking for treasure of this forest"')
                time.sleep(2)
                print('You stay silent')
                print('She says, "Answer this question and I will open the path to the treasure you seek."')
                time.sleep(2)
                print('In the heart, I dwell, a gentle embrace,')
                print('I brighten the world, bringing smiles to each face.')
                time.sleep(2)
                print('Though small in my form, my power is vast,')
                print('A simple act shared can forever last.')
                answer = input('What am I?: ')
                if answer.lower() == 'kindness':
                    print('Ah yes, I am glad you are a gentle soul and understand the power of kindess')
                    print('I open the path for you.')
                    time.sleep(2)
                    print('You walk through the waterfall')
                    print('And with all its glory you find the treasure of Awwe!')
                    time.sleep(2)
                    print('Congratulations, with your curiosity and kindess you were able to complete your journey')
                    print('You have won the Game!')
                else:
                    print('The elf looks dissapointed')
                    print('She than says "I can not help you on this journey"')
                    time.sleep()
                    print('"If you can not understand kindness there is not path to hapiness in your life."')
                    print('You then leave the lake and continue wandering into the forest.')
                    time.sleep()
                    print('Unable to find the treasure you decide to leave the forest')
                    print('Though your tale did not end in glory and victory')
                    time.sleep()
                    print('You are left with a question of life and hapiness')
                    print('There is always a chance to grow and learn')
                    time.sleep()
                    print('Game Over')
        else:
            print('You decide to not engage with the elf')
            print('Instead you decide to continue along the route set on your map.')
            time.sleep(2)
            print('But without your compass, you find it harder to locate the direction you need to go in')
            print('The tall trees block the sky above you giving you any sense of direction.')
            time.sleep(2)
            print('still you persevere through the forest eventually leading you outside.')
            print('You returned back from where you started.')
            time.sleep(2)
            print('confused and exhuasted, you decide to go back to the nearest town.')
            print('Telling your stories of the gigantic spider and enchanted elf')
            time.sleep(2)
            print('Although the treasure was not found. The treasure of a story will suffice')
            print('Game Over')


#choice 1 continues

