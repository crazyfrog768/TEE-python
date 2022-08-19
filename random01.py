import math
import random

damage = random.randint(50, 70)
print(damage)

per = random.uniform(0, 100)
print(per)

if per < 22.5:
    print('it is damaged !!')
    damage *= 2

print(damage)

print('---------------------------------------')
# random from LIST
moneys = [0, 20, 100, 1000]
money = random.choice(moneys)
print(moneys)
random.shuffle(moneys)
print(moneys)

print('---------------------------------------')
