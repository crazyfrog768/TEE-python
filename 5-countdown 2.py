# ---------------------------------------------------------
#   *** Fun with countdown ***
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise: Chapter : 1 - item : 5 - Countdown มหาสนุก
# ---------------------------------------------------------

print(" *** Fun with countdown ***")

ls = [int(e) for e in input("Enter list : ").split()]
#print(ls, 'len(ls) is : ', len(ls))

total_countdown = 0
new_list =[]
sum_list =[]
this_list_is_OK = False
last_countdown_status = False
i = 0

while i < len(ls):
    the_second = -1
    the_first = int(ls[i])
#    print('i is >> ', i)
    if the_first == 1 and i < len(ls)  and this_list_is_OK == False and last_countdown_status == False:
        this_list_is_OK = False
        new_list.append(ls[i])
        sum_list.append(new_list)
#        print('if the_first==1  i:', i, the_first, the_second, ' new_list: ', new_list, 'sum_list: ', sum_list, this_list_is_OK, last_countdown_status)
        new_list = []
        total_countdown += 1
    elif the_first <= 0 :
            new_list = []
            exit
    if i+1 < len(ls):
        if this_list_is_OK == False :
                #and last_countdown_status == False:
            new_list.append(ls[i])
        if i < (len(ls))-1:
           the_second = int(ls[i+1])
        else:
           the_second = int(ls[i])

#        print('i+1 < len(ls) >> new_list : ', new_list)
        if (the_first - the_second) == 1:
            this_list_is_OK = True
            last_countdown_status = True
            new_list.append(ls[i+1])
#            print('inside  i:', i, the_first, the_second, ' new_list: ', new_list, 'sum_list: ', sum_list, this_list_is_OK, last_countdown_status)
        else:
            new_list = []
            this_list_is_OK = False
        if int(ls[i+1] == 1) and this_list_is_OK == True:
            this_list_is_OK = False
            last_countdown_status = False
            sum_list.append(new_list)
            new_list = []
            total_countdown += 1
            i += 1
            exit
    i += 1
#    print('outside  i:', i, the_first, the_second, ' new_list: ', new_list, 'sum_list: ', sum_list, this_list_is_OK, last_countdown_status)

temp_list = []
temp_list.append(sum_list)
#print('temp_list  ---> ', temp_list)
#print('sum_list  ---> ', sum_list)
sum_list = temp_list
sum_list.insert(0, total_countdown)
print(sum_list)