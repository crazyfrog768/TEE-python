# ---------------------------------------------------------
#  *** Summation of each digit ***
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise: Chapter : 1 - item : 3 - loop
# ---------------------------------------------------------
print(' *** Summation of each digit ***')

temptext = input('Enter a positive number : ')
sum_digit = 0
#print(temptext)     # for debugging

len_string = len(temptext)

for i in range (len_string):
#    print(temptext[i])
    sum_digit += int(temptext[i])

print('Summation of each digit = ', sum_digit)





