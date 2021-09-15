import random
number = random.randint(1, 9)
chances = 0

print("❓🧠The Number Guesser - a math riddle based game🎲🧮")

print("Welcome to The Number Guesser. Here you will be shown a riddle and solving it will give you a numerical answer. Type that in the space given and pass the test. You have 5 chances to guess the correct number. Good Luck!!!")

if number == 1:
    print("✖️ ➕What three numbers, none of which is zero, give the same result whether they’re added or multiplied? Type in the least number in them? ➖ ➗")

if number == 2:
    print("🍎🍎If there are three apples and you take away two, how many apples do you have?🍏🍏")

if number == 3:
    print("👧🏼👧🏽👩‍🦰A man describes his daughters, saying, “They are all blonde, but two; all brunette but two; and all redheaded but two.” How many daughters does he have?👧🏼👧🏽👩‍🦰")

if number == 4:
    print("🐢🐠Leon works at the aquarium. When he tries to put each turtle in its own tank, he has one turtle too many. But if he puts two turtles per tank, he has on tank too many. How many turtles and how many tanks does Leon have? Type in the number of turtles he has🐢🐠")

if number == 5:
    print("👩‍👧‍👧Mary has four daughters, and each of her daughters has a brother. How many children does Mary have?👩‍👧‍👧")

if number == 6:
    print("🚴‍♂️🦟Two cyclists began a training run, one starting from Moscow and the other starting from Simferopol. When the riders were 180 miles apart, a fly took an interest. Starting on one cyclists shoulder, the fly flew ahead to meet the other cyclist. After reaching him the fly then turned around and yet back. The restless fly continued to shuttleback and fourth until the pair met; then settled on the nose of one rider. The flys speed was 30 mph. Each cyclist speed was 15 mph. How many miles did the fly travel?🚴🏽‍♂️🦟")

if number == 7:
    print("🧮🔢I am an odd number. Take away a letter and I become even. What number am I?🔢🧮")

if number == 8:
    print("⚖️🥔How much is this bag of potatoes?' asked the man. '32lb divided by half its own weight,' said the green grocer. How much did the potatoes weigh?🥔⚖️")

if number == 9:
    print("👨‍👧🔞Charlotte is 13 years old. Her father Montague is 40 years old. How many years old was Charlotte when her father was four times as old as Charlotte?🔞👨‍👧")



while chances<5:
    
    guess = int(input("enter a num 🔢:-"))

    if guess == number:
        print("🏆Congrats you won🏆")
        break

    elif guess<number:
        print("⛔guess was too low⛔")

    else:
        print("⛔guess was too high⛔")

    chances +=1


if not chances < 5:
    print("🙁Aw man. You were so close! The number was : ", number)


print("😃Do you want to play again and discover more math riddles. Type '1' to play again.  If you want to exit, type '2' 😃")
choice = int(input("🤔What do you choose. Yes or No🤔 :"  ))



if choice <2:
    print("💐Welcome back. Press the up arrow key and hit enter to join in again.💐")


else:
    print("👋Goodbye. See you later👋")

        