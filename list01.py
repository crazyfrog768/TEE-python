q1 = 'ปลูกต้นมะม่วง'
q2 = 'ล้วงปลาไหล'
q3 = 'ไล่ศัตรูพืช'

quests = ['ปลูกต้นไม้', 'ปลาไหล', 'ถากศรัตรูพื้ช']

print(quests)
print('--------------------------------------')
for i in range(0, 3, 1):
    if i == 1:
        quests[i] = 'ขุดสระ'
    print(quests[i])

print('--------------------------------------')
print(quests)

quests.append('ปลูกป่า')
print(quests)

quests.insert(2, 'ภูเขา')
print(quests)

quests.remove('ภูเขา')
print(quests)
print('--------------------------------------')

quests.insert(3, 'ภูเขา')
print(quests)
if 'ภูเขา' in quests:
    print('OK .... ')

max_quests = 10
if len(quests) < max_quests:
    quests.append('จับปลาดุก')
    print(quests, '\nand ', 'Len quests is ', len(quests))

print('--------------------------------------')
for i in range(0, len(quests), 1):
    print(str(i+1), ' : ', quests[i])
