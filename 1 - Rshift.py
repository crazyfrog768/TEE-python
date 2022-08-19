# ---------------------------------------------------------
#   สร้างฟังชั่น right shift
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise:    Chapter : 2 - item : 1 - Rshift
# ---------------------------------------------------------

def Rshift(num,shift):
    return num >> shift

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))