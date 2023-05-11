import random
print('Hello, this is dice roll(D6)!')
i = 1
status = True
error = 0
error2 = 0
while True:
    try:
        dice_num = int(input('How many die are you rolling today?: '))
        error = 0 #resetting error count
        if dice_num < 0:
            print('Your die disappeared into the void. Thankfully, we got some extra you can use.')
            continue
        elif dice_num == 0:
            print('You rolled NOTHING! It\'s okay, let\'s get you some die.')
            continue
        break
    except ValueError:
        print('What? Can you give me an integer?')
        error += 1
        if error > 4:
            print('I give up... Goodbye!')
            status = False
            break
while status == True:
    total = 0
    while i <= dice_num:
        dice_value = random.randint(1,6)
        print(f'Dice {i}: {dice_value}')
        total += dice_value
        i += 1
    if dice_num > 0:
        print(f'Total Sum: {total}')
    response_status = True
    
    if dice_num > 0:
        while response_status == True:
            response = input('Roll again?(Y/N). To change dice count(C): ')
            if response.lower() == 'y' or response.lower() == 'yes':
                status = True
                response_status = False
            elif response.lower() == 'n' or response.lower() == 'no':
                status = False
                response_status = False
            elif response.lower() == 'c':
                while True:
                    try:
                        dice_num = int(input('How many die are you rolling this time?: '))
                        error2 = 0
                        if dice_num < 0:
                            print('Your die disappeared into the void. Thankfully, we got some extra you can use.')
                            continue
                        elif dice_num == 0:
                            print('You rolled NOTHING! It\'s okay, let\'s get you some die.')
                            continue
                        else:
                            break
                    except ValueError:
                        print('What? Can you give me an integer?')
                        error2 += 1
                        if error2 > 4:
                            print('I give up... Goodbye!')
                            status = False
                            response_status = False
                            break
                break
            else:
                print('What? Please answer in (Y/N) format.')
    i = 1 #resetting dice roll
if error <=4 and error2 <= 4:
    print('Keep the good times rolling, my friend!')