import random

k = "0"
r = random.randint(1,100)
print(r) #cheating

while True:
    k=str ( int(k) + 1 )
    guess = int ( input ( "Guess "+ k +":" ) )
    if guess < r:
        print("Clue: higher")
    elif guess > r:
        print("Clue: lower")
    elif guess == r:
        print("Correct answer after only "+ k +" guesses - Excellent!")
        break
    