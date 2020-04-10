#Python Programming
#ITM (CWN Series)

#Module Random
#random.random()
#random.uniform()
#random.randrange()
#random.choice()
#random.sample()

import random
x=random.random()               # Random float x, 0.0 <= x < 1.0
print(x)

x=random.uniform(1, 10)         # Random float x, 1.0 <= x < 10.0
print(x)

x=random.randrange(10)         # Integer from 0 to 9
print(x)

x=random.randrange(0, 101, 2)  # Even integer from 0 to 100
print(x)

x=random.choice('abcdefghij')   # Single random element
print(x)

items = [1, 2, 3, 4, 5, 6, 7]
print(items)
random.shuffle(items)
print(items)

sam=random.sample([1, 2, 3, 4, 5], 3) # Three samples without replacement
print(sam) 
output = [2, 3, 1] #3 random numbers


#Mini game with module random
import random
num = random.randint(1,20)
name = input("Give me your Name: ")
print("Can you guess my number? ")
print("Let's Check This")
guess = 0
tries = 0
while guess!=num:
    try:
        guess = int(input("Give me the number: "))
        tries = tries + 1
        if guess > num:
            print("Your number is greater!")
        if guess < num :
            print("Your number is lower!")
    except:
        break
if tries >=1 and guess==num:
    print("Congrats",name,"/ Your Tries: ",tries)
else:
    print("!Error!")
