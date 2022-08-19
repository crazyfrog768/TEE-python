import tank
import tkinter as tk

first_tank = tank.Tank('russiaK1', 3)
print(first_tank.ammo)
print(first_tank.name)

print('---------------------------')
first_tank.name = 'ThailandA1111'
print(first_tank.name)
print(first_tank.ammo)
first_tank.add_ammo(2)
print(first_tank.name)
print(first_tank.ammo)
print('---------------------------')
second_tank = tank.Tank('ChinaBBB222', 3)
print(second_tank.name)
print(second_tank.ammo)
second_tank.add_ammo(10)
print(second_tank.ammo)

print('---------------------------')
# method of class (class method)
print('Before firing: ', first_tank.ammo)
first_tank.fire_ammo()
print('after firing: ', first_tank.ammo)

print('Before 2 firing: ', first_tank.ammo)
first_tank.fire_ammo()
first_tank.fire_ammo()
print('after 2 firing: ', first_tank.ammo)
first_tank.add_ammo(4)
print('first_tank.add_ammo(4) : ', first_tank.ammo)