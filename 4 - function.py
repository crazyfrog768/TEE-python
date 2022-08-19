# ---------------------------------------------------------
#    ***Function Odd List***
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise: Chapter : 1 - item : 4 - function
# ---------------------------------------------------------

def odd_list(alist):
    temp_list = []
    for i in range (0, len(alist)):
        if alist[i] % 2 != 0:
            temp_list.append(int(alist[i]))
    return temp_list

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
#print(ls)
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

