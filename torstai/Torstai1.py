import random

numerot = []
for x in range(10):
    numerot.append(random.randrange(1,100))
numerot.sort(reverse=True)
print(numerot)
