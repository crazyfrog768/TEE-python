print("hello Tee")
print('what is double quote or single quote')

a = 10
b = 11.1
c = a + b
print('C is ', c)
print('********************************************')
print()

score = 78
if score >= 80:
    printf('Grade: A')
    printf("Yes")
elif score >= 70 :
    print('Grade B')
else:
    print('Grade C')

print('********************************************')
print()

for i in range(3):
    print(i)
print('-----------------')
for i in range(1,3):
    print(i)
print('-----------------')
for i in range(1, 9, 3):
    print(i)
print('-----------------')
for i in range(1, 9):
    if i % 3 == 0:
        continue
    print(i)

print('********************************************')
print()
w = 4
l = 4
h =2
cube = w*l*h
print('vel is ', cube)

def getvol(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    return a*b*c
print('-----------------')
print('vol is >>> ', getvol(w, l, h))

print('embeded value to function .>>> ', getvol(a = 3, b =3, c= 5))
print('-----------------')
boxvol1 = getvol(10, 30, 2)
print('boxvol1 = ', boxvol1)

print('-----------------')
boxvol2 = getvol(10, -5, 2)
print('boxvol2 (contain <= 0)  = ', boxvol1)

print('********************************************')
print()

import shape

circle = shape.get_circle_area(10)
print('circle is ', circle)

triangle = shape.get_triangle_area(10, 32)
print('triangle is ', triangle)
