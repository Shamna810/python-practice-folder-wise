import random
secret = random.randint(1,30)
while True:
    guess = int(input("enter your guess:"))
    
    if guess==secret:
       print("both matched")
       break
    elif secret>guess:
        print("too low")
    else:
        print("too high") 