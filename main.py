import random

print('*********************************')
print('Welcome to the guessing game!')
print('*********************************')

secret_number = random.randint(0, 10)

def show_message():

    global hint_str, hint

    hint_str = input('Guess a number between 0 and 10: ')
    hint = int(hint_str)

    validate_number()

def validate_number():

    hit       = hint == secret_number
    miss_more = hint >  secret_number
    miss_less = hint <  secret_number

    if hint < 0 or hint > 10:
        print("Please insert a number between 0 and 10.")
        show_message()

    else:

        global game_over
        game_over = False

        while game_over == False:

            if hit:
                print("You guess it! The secret number is {}!".format(secret_number))
                game_over = True

            elif miss_more:
                print("You miss it! A little bit lower.")
                game_over = False
                show_message()
            
            elif miss_less:
                print("You miss it! A little bit higher.")
                game_over =  False
                show_message()

show_message()

