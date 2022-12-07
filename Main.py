"""
This code makes it so you can play Blackjack.
"""
# James Holloway This program is supposed to simulate a game of black jack I
# got help from Prof. Brown on a lot of this project and got help from the
# Teacher assistants while I was working on this project.
import random


def instructions():
    """
The instructions for the game blackjack.
    """
    good_input = 1
    while good_input == 1:
        try:
            instructions_input = int(input("If you want to see the "
                                           "instructions to blackjack enter "
                                           "1, if not then enter 0"))
            if instructions_input == 1:
                print("This game is called blackjack")
                print(
                    "In blackjack you start off with two cards and depending "
                    "on "
                    "what the cards are",
                    "\nyou will decide whether you want to hit(ask for "
                    "another "
                    "card) or stay(don't ask for another card)")
                print(
                    "The point of this game is to get your hand(your cards) "
                    "closer "
                    "to 21 than the", "\ndealers hand")
                good_input = 0

            elif instructions_input == 0:
                print("Ok")
                good_input = 0

            else:
                print("Please enter a 1 or a 0.")
        except ValueError:
            print("Please enter a 1 or a 0.")


def generate_card():
    """
This generates your card
    :return:
    """
    # for x in range(10): this is here, so I can run something multiple times
    # to see if it runs correctly
    good_input = 1
    card = random.randint(1, 52)
    if card == 1:
        x = 0
        while good_input == 1:
            try:
                while x == 0:
                    try:
                        value = int(
                            input("You got the Ace of Spades, do you want it "
                                  "to "
                                  "equal 1 or 11?"))
                        if value == 1:
                            card = 1
                            x = 1
                            good_input = 0
                        elif value == 11:
                            card = 11
                            x = 1
                            good_input = 0
                        else:
                            print("Please pick 1 or 11.")
                    except ValueError:
                        print("Please enter a 1 or 11.")
            except ValueError:
                print("Please enter a 1 or 11.")

    elif card == 13:
        card = 10
        # print(format("King of Spades"), end = '')
    elif card == 12:
        card = 10
        # print(format("Queen of Spades"), end='')
    elif card == 11:
        card = 10
        # print(format("Jack of Spades"), end='')
    # I use "elif" instead of an "if" statement because if I use "if"
    # statements then the code will keep trying to run something that isn't
    # supposed to run.
    elif 15 <= card <= 23:
        value = card - 13
        return value
    elif card == 14:
        x = 0
        while good_input == 1:
            try:
                while x == 0:
                    try:
                        value = int(
                            input("You got the Ace of Diamonds, do you want "
                                  "it to "
                                  "equal 1 or 11?"))
                        if value == 1:
                            card = 1
                            x = 1
                            good_input = 0
                        elif value == 11:
                            card = 11
                            x = 1
                            good_input = 0
                        else:
                            print("Please pick 1 or 11.")
                    except ValueError:
                        print("Please enter a 1 or 11.")
            except ValueError:
                print("Please enter a 1 or 11.")
    elif card == 26:
        card = 10
        # print(format("King of Diamonds"), end='')
    elif card == 25:
        card = 10
        # print(format("Queen of Diamonds"), end='')
    elif card == 24:
        card = 10
        # print(format("Jack of Diamonds"), end='')

    elif 28 <= card <= 36:
        value = card - 26
        return value

    elif card == 27:
        x = 0
        while good_input == 1:
            try:
                while x == 0:
                    try:
                        value = int(
                            input("You got the Ace of Hearts, do you want it "
                                  "to "
                                  "equal 1 or 11?"))
                        if value == 1:
                            card = 1
                            x = 1
                            good_input = 0
                        elif value == 11:
                            card = 11
                            x = 1
                            good_input = 0
                        else:
                            print("Please pick 1 or 11.")
                    except ValueError:
                        print("Please enter a 1 or 11.")
            except ValueError:
                print("Please enter a 1 or 11.")

    elif card == 39:
        card = 10
        # print(format("King of Hearts"), end='')
    elif card == 38:
        card = 10
        # print(format("Queen of Hearts"), end='')
    elif card == 37:
        card = 10
        # print(format("Jack of Hearts"), end='')

    elif 41 <= card <= 49:
        value = card - 39
        return value
    # this makes it so if it's a number card it will display the card number
    # instead of the randomly generated number.
    elif card == 40:
        x = 0
        while good_input == 1:
            try:
                while x == 0:
                    try:
                        value = int(
                            input("You got the Ace of Clubs, do you want it "
                                  "to "
                                  "equal 1 or 11?"))
                        if value == 1:
                            card = 1
                            x = 1
                            good_input = 0
                        elif value == 11:
                            card = 11
                            x = 1
                            good_input = 0
                        else:
                            print("Please pick 1 or 11.")
                    except ValueError:
                        print("Please enter a 1 or 11.")
            except ValueError:
                print("Please enter a 1 or 11.")

    elif card == 52:
        card = 10
        # print(format("King of Clubs"), end='')
    elif card == 51:
        card = 10
        # print(format("Queen of Clubs"), end='')
    elif card == 50:
        card = 10
        # print(format("Jack of Clubs"), end='')
    # these make it so instead of printing the number of the card or the
    # randomly generated number, the code will output the name of the card
    # since these are face cards.
    return card


def generate_dealer_card():
    """
This generates the dealer's card
    :return:
    """
    # for x in range(10):
    card = random.randint(1, 52)
    if card == 1:
        card = 11
    elif card == 13:
        card = 10
    elif card == 12:
        card = 10
    elif card == 11:
        card = 10
    # I use "elif" instead of an "if" statement because if I use "if"
    # statements then the code will keep trying to run something that isn't
    # supposed to run.
    elif 15 <= card <= 23:
        value = card - 13
        return value

    elif card == 14:
        card = 11
    elif card == 26:
        card = 10
    elif card == 25:
        card = 10
    elif card == 24:
        card = 10

    elif 28 <= card <= 36:
        value = card - 26
        return value

    elif card == 27:
        card = 11
    elif card == 39:
        card = 10
    elif card == 38:
        card = 10
    elif card == 37:
        card = 10

    elif 41 <= card <= 49:
        value = card - 39
        return value
    # this makes it so if it's a number card it will display the card number
    # instead of the randomly generated number.
    elif card == 40:
        card = 11
    elif card == 52:
        card = 10
    elif card == 51:
        card = 10
    elif card == 50:
        card = 10
    # these make it so instead of printing the number of the card or the
    # randomly generated number, the code will output the name of the card
    # since these are face cards.
    return card


def requirements():
    """
These are the requirements for the project.
    """
    print(15 * 5)
    # this is multiplication
    print(15 ** 5)
    # this is powers
    print(15 / 5)
    # this is division
    print(15 % 5)
    # this is modulus operator divides two numbers and gives you the
    # remainder, kind of like long division
    print(15 // 5)
    # this is floor division rounds the answer to the nearest integer
    print(15 + 5)
    # this is addition
    print("This is" + " my code.")
    # the plus sign adds the two strings together
    print("This is my code" * 2)
    # the multiplication sign makes it so the print repeats two times
    print(format("This is my code"), end='')
    # this makes it so the next line of code displays right after it
    print("Cost: $", format("12.00"), sep="")
    # this makes it so the whitespace is removed between "$" and "12.00"
    your_name = input("What is your name?")
    print(your_name)
    # inputs your name then displays it
    if your_name == "james" or your_name == "James":
        print("Your name is james")
    else:
        print("Your name is not james")
    # if the name you put in is james then the program tells you your name
    # is james, if you didn't enter james it'll tell you your name isn't james
    # the or makes it, so it catches both James and james
    sports = ("soccer", "basketball", "football")
    if "soccer" in sports:
        print("yes")
    # if the thing you said is in the list then it outputs what you want it to


def requirement2(first_name, last_name):
    """
One of the requirements
    :param first_name:
    :param last_name:
    """
    print(first_name + " " + last_name)


def players_hand():
    """
Creates the player's hand.
    :return:
    """
    card1 = int(generate_card())
    card2 = int(generate_card())
    total = int(card1 + card2)
    print("You got a", card1, "and a", card2)
    x = 1
    good_input = 1
    while good_input == 1:
        try:
            while x == 1:
                if total > 21:
                    total = 0
                    x = 0
                    good_input = 0
                elif total < 21:
                    value = int(
                        input("If you want another card enter 1,if not enter "
                              "0 "))
                    if value == 1:
                        total += generate_card()
                        print(total)
                        good_input = 0
                    elif value == 0:
                        x = 0
                        good_input = 0
                    else:
                        print("Please enter a 1 or 0.")
        except ValueError:
            print("Please enter a 1 or 0.")
    return total


def dealers_hand():
    """
This creates the dealer's hand.
    :return:
    """
    first_card = generate_dealer_card()
    second_card = generate_dealer_card()
    total = first_card + second_card
    print(
        "The dealer has two cards one is facing down, and the other one is a",
        first_card)
    return total


def main():
    """
This is the code that makes the actual game.
    """
    instructions()
    dealer_hand = dealers_hand()
    while dealer_hand < 16:
        dealer_hand += generate_dealer_card()
    if dealer_hand > 21:
        dealer_hand = 0
    player_hand = players_hand()
    print("Since the dealer's hand is under 16 they have to get another card.")
    if player_hand > dealer_hand:
        print("You got ", player_hand)
        print("The dealer got ", dealer_hand)
        print("You have won.")
    elif player_hand < dealer_hand:
        print("You got ", player_hand)
        print("The dealer got ", dealer_hand)
        print("You have lost.")
    elif player_hand == dealer_hand:
        print("You got ", player_hand)
        print("The dealer got ", dealer_hand)
        print("you have tied with the dealer.")
    else:
        print("You should not be able to see this.")


requirement2("James", "Holloway")
main()
# x = 1
# while x == 1:
# input = int(input("If you want to play again enter 1, if not enter 0."))
# if input == 1:
# main()
# if input == 0:
# x = 0


z = 0
while z != 1:
    answer = int(input(
        "Enter 1 to see the requirements for the project, enter 2 if you "
        "dont want to see them."))
    if answer == 1:
        requirements()
        z = 1
    elif answer == 2:
        print("Ok")
        z = 1
    else:
        print("Lets try that again.")
# this is here, so you can see the requirements being run if you want to
