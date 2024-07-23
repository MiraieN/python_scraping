import random
import time


# function to center texts
def center(txt):
    return txt.center(50)


def points(point, who):
    if point == 1:
        print(center(f'\n{who} have {point} point'))
    else:
        print(center(f'\n{who} have {point} points'))


# meeting
print(center("Hello!"))
print(center("I am RSP bot, nice to meet you"))
user_in = input(center("let's play a game, wanna start? (Y/N)\n")).lower()
# cycling if no
while user_in == "n" or user_in == "no":
    print(center("hmm... maybe you could overthink?"))
    print(center("I will give you time"))
    for count in range(3, 0, -1):
        print(f'{count}...')
        time.sleep(1)
    user_in = input(center("wanna start? (Y/N)\n")).lower()
    if user_in == "y" or user_in == "yes":
        print(center("Grrrand idea!"))

#rules
print(center("So, the rules:"))
print(center("U pick one of these (rock, paper, scissors) and I pick randomly"))
print(center("I generate all of them at once so u can check am I honest with randoming it"))
print(center("just type show_items"))

# generating items for game
items = ["rock", "scissors", "paper"]
random.shuffle(items)
bot_score, user_score, count = 0, 0, -1
item_pos = 0

# main game
while user_score != 3 or bot_score != 3:
    count += 1
    print(center(f'Round {count+1}'))
    user_in = input("What would u pick? (R/S/P)\n").lower()
    # if user_in == "show_items":
    #     print(center("This game I will pick it next way:"))
    #     for num in range(3):
    #         print(center(f'{num+1} round: {items[num]}'))
    #     user_in = input("So, what would u pick? (R/S/P)\n").lower()
    poss_items = ("rock", "r", "paper", "p", "scissors", "s")

    while user_in not in poss_items:
        print(center("U typed it wrong. Try again"))
        user_in = input("What would u pick? (R/S/P)").lower()

    item_pos += 1
    try:
        print(center(f'I got {items[item_pos]}'))
    except IndexError:
        random.shuffle(items)
        item_pos = 0
        print(center(f'I got {items[item_pos]}'))

    # checking if random got rock
    if user_in in poss_items[0:2]:
        if items[item_pos] == "rock":
            print(center("We've got the same"))
        elif items[item_pos] == "scissors":
            user_score += 1
        elif items[item_pos] == "paper":
            bot_score += 1
    # if paper
    if user_in in poss_items[2:4]:
        if items[item_pos] == "paper":
            print(center("We've got the same"))
        elif items[item_pos] == "rock":
            user_score += 1
        elif items[item_pos] == "scissors":
            bot_score += 1
    # if scissors
    if user_in in poss_items[4:6]:
        if items[item_pos] == "scissors":
            print(center("We've got the same"))
        elif items[item_pos] == "paper":
            user_score += 1
        elif items[item_pos] == "rock":
            bot_score += 1

    # printing points
    points(user_score, "U")
    points(bot_score, "I")

    # if someone got 2 points first, finishing game
    if user_score == 2 and bot_score != 2:
        print(center("U won. Congratz!"))
        break
    if bot_score == 2 and user_score != 2:
        print(center("I won. He-he"))
        break

    print(center("Let's go the next round"))

# end check. The one with 3 points wins
if user_score == 3 and bot_score != 3:
    print(center("U won. Congratz!"))
elif bot_score == 3 and user_score != 3:
    print(center("I won. He-he"))
