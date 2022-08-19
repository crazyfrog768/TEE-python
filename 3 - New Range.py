# ---------------------------------------------------------
#    Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function
#     *** New Range ***
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise:    Chapter : 2 - item : 3 - New Range
# ---------------------------------------------------------
def new_range(a, b, c):
    i = round(a, 3)
    local_list = []
    while i < b:
        local_list.append(i)
#        print('c: ', c, ' , i : ', i, local_list)
        i = round(i,3) + round(c, 3)
        i = round(i,3)
    return  local_list


ls = [float(e) for e in input("Enter Input : ").split()]
argument_case = len(ls)
#print(argument_case, '  ::: ', ls[0])

my_list = []

if argument_case == 1:
    #print(ls[0])
    my_list = new_range(0.0, ls[0], 1.0)
elif argument_case == 2:
    #print(ls[0], ' : ', ls[1])
    my_list = new_range(ls[0], ls[1], 1.0)
elif argument_case == 3:
    my_list = new_range(ls[0], ls[1], ls[2])

print(tuple(my_list))
