import random

playerhand = random.randint(1,10) + random.randint(1,10)
dealerhand = random.randint(1,10) + random.randint(1,10)

while dealerhand < 17:
    dealerhand = dealerhand + random.randint(1,10)
    print(dealerhand)                