import random
number = random.randint(1, 9)
chances = 0

print("โ๐ง The Number Guesser - a math riddle based game๐ฒ๐งฎ")

print("Welcome to The Number Guesser. Here you will be shown a riddle and solving it will give you a numerical answer. Type that in the space given and pass the test. You have 5 chances to guess the correct number. Good Luck!!!")

if number == 1:
    print("โ๏ธ โWhat three numbers, none of which is zero, give the same result whether theyโre added or multiplied? Type in the least number in them? โ โ")

if number == 2:
    print("๐๐If there are three apples and you take away two, how many apples do you have?๐๐")

if number == 3:
    print("๐ง๐ผ๐ง๐ฝ๐ฉโ๐ฆฐA man describes his daughters, saying, โThey are all blonde, but two; all brunette but two; and all redheaded but two.โ How many daughters does he have?๐ง๐ผ๐ง๐ฝ๐ฉโ๐ฆฐ")

if number == 4:
    print("๐ข๐ Leon works at the aquarium. When he tries to put each turtle in its own tank, he has one turtle too many. But if he puts two turtles per tank, he has on tank too many. How many turtles and how many tanks does Leon have? Type in the number of turtles he has๐ข๐ ")

if number == 5:
    print("๐ฉโ๐งโ๐งMary has four daughters, and each of her daughters has a brother. How many children does Mary have?๐ฉโ๐งโ๐ง")

if number == 6:
    print("๐ดโโ๏ธ๐ฆTwo cyclists began a training run, one starting from Moscow and the other starting from Simferopol. When the riders were 180 miles apart, a fly took an interest. Starting on one cyclists shoulder, the fly flew ahead to meet the other cyclist. After reaching him the fly then turned around and yet back. The restless fly continued to shuttleback and fourth until the pair met; then settled on the nose of one rider. The flys speed was 30 mph. Each cyclist speed was 15 mph. How many miles did the fly travel?๐ด๐ฝโโ๏ธ๐ฆ")

if number == 7:
    print("๐งฎ๐ขI am an odd number. Take away a letter and I become even. What number am I?๐ข๐งฎ")

if number == 8:
    print("โ๏ธ๐ฅHow much is this bag of potatoes?' asked the man. '32lb divided by half its own weight,' said the green grocer. How much did the potatoes weigh?๐ฅโ๏ธ")

if number == 9:
    print("๐จโ๐ง๐Charlotte is 13 years old. Her father Montague is 40 years old. How many years old was Charlotte when her father was four times as old as Charlotte?๐๐จโ๐ง")



while chances<5:
    
    guess = int(input("enter a num ๐ข:-"))

    if guess == number:
        print("๐Congrats you won๐")
        break

    elif guess<number:
        print("โguess was too lowโ")

    else:
        print("โguess was too highโ")

    chances +=1


if not chances < 5:
    print("๐Aw man. You were so close! The number was : ", number)


print("๐Do you want to play again and discover more math riddles. Type '1' to play again.  If you want to exit, type '2' ๐")
choice = int(input("๐คWhat do you choose. Yes or No๐ค :"  ))



if choice <2:
    print("๐Welcome back. Press the up arrow key and hit enter to join in again.๐")


else:
    print("๐Goodbye. See you later๐")

        