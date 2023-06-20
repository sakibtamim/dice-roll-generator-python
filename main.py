import random

def roll_dice():

    while True:
        min_val = 1
        max_val = 6

        num_dice = input(f"Number of dice: '1' or '2'\n"
                         f"Choose: ")


        if num_dice == '2':
            print("Rolling dice...")
            dice_1 = random.randint(min_val, max_val)
            dice_2 = random.randint(min_val, max_val)

            print("The values are:")
            print("Dice one:", dice_1)
            print("Dice two:", dice_2)
            print("total: ", dice_1 + dice_2)

            roll_again = input("Roll again: 'yes' or 'no \n:")
            if roll_again == 'no':
                print('Thank you')
                break


        elif num_dice == '1':
            print("Rolling dice...")
            dice_1 = random.randint(min_val, max_val)

            print("Dice one:", dice_1)

            roll_again = input("Roll again: 'yes' or 'no' \n:")
            if roll_again == 'no':
                print('Thank you')
                break

if __name__ == '__main__':
    roll_dice()