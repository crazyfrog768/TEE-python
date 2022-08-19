file = open('scores.txt')

print('-------------------')
print(file.read())
print('-------------------')

file = open('scores.txt')
print('readline: ', file.readline())

file = open('scores.txt')    # reset to first line
for score in file:
    print(score)         # there is extra line space ...

print('---------------------------------------')
file = open('scores.txt')    # reset to first line
pass_count = 0
for score in file:
    if int(score) > 50:
        pass_count += 1
print('pass 50 : ', pass_count)

file.close()