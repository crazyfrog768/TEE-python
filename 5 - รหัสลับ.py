# ---------------------------------------------------------
#    ตึกลึกลับแห่งหนึ่งเมื่อเดินไปข้างหลังจะมีคนบอกรหัสลับมาจงสร้างฟังชั่นคำนวณรหัส
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise:    Chapter : 2 - item : 5 - รหัสลับ
# ---------------------------------------------------------
def bon(w):
    temp_char = w[0]
    found_char = '\n'
    i = 1

    while i <= len(w) :
        if temp_char == w[i]:
            found_char = w[i]
#            print("yes ...", type(found_char))
            break
        else:
            temp_char = w[i]
#            print('i is: ', i, ' w[i] > ', w[i], ' temp_char >>> ', temp_char, '   found_char >> ', found_char)
            i += 1

    unicode_a = ord('a')
    unicode_bon = ord(found_char[0])
    the_code = (unicode_bon - unicode_a + 1)*4
    return the_code

secretCode = input("Enter secret code : ")
print(bon(secretCode))

