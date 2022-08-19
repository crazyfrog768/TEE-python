# ---------------------------------------------------------
# use simple math to calculate hh*60*60 + mm *60 + sec
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise: Chapter : 1 - item : 1 - รับ h m s --> คำนวณวินาที
# ---------------------------------------------------------
print('*** Converting hh.mm.ss to seconds ***')
temptext = input('Enter hh mm ss : ')
temptext_list = temptext.split(' ')
# print(temptext)
#for eachtext in temptext_list:  # now loop the list
#    eachnum = int(eachtext)
#    print(eachnum, end="-")
#print()

any_error = False
total_sec = 0
result_text =''
for i in range (len(temptext_list)):
    eachnum = int(temptext_list[i])
    if i < len(temptext_list):
        if eachnum < 10:
            result_text += '0'+temptext_list[i] + ":"
        else:
            result_text += temptext_list[i] + ":"
    else:
        result_text += temptext_list[i]
    # print(eachnum, end='-')             # for testing / debug
    if i == 0 and any_error == False:
        if eachnum < 0:
            any_error = True
            temp_text = 'hh(' + temptext_list[i].strip()  + ') is invalid!'
            print(temp_text)
            exit
        else:
            total_sec += eachnum * 60*60
    elif i == 1 and any_error == False :
        if eachnum >= 60 or eachnum < 0:
            any_error = True
            temp_text = 'mm(' +  temptext_list[i].strip() + ') is invalid!'
            print(temp_text)
            exit
        else:
            total_sec += eachnum *60
    elif i == 2 and any_error == False:
        if eachnum >= 60 or eachnum < 0:
            any_error = True
            print('ss(', temptext_list[i].strip(), ') is invalid!')
            exit
        else:
            total_sec += eachnum

temp_text = result_text.rstrip(":")
if any_error == False:
    print(temp_text, '=', f"{total_sec:,}", 'seconds')