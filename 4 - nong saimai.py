# ---------------------------------------------------------
#    หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise:    Chapter : 2 - item : 4 - nong saimai
# ---------------------------------------------------------
def hbd(age):
    my_base = 3
    while my_base > 2:
        value1 = 0 + my_base * 2
        value2 = 1 + my_base * 2
        if (value1 == age):
            temp_str = 'saimai is just 20, in base ' + str(my_base) + '!'
            break
        if (value2 == age):
            temp_str = 'saimai is just 21, in base ' + str(my_base) + '!'
            break

        my_base += 1
    return temp_str

y = input("Enter year : ")
year = int(y)

print(hbd(int(year)))

