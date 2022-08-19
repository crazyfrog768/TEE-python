# ---------------------------------------------------------
# use simple math to calculate wind classification
#
#  Name: sorawit loeyvanicharoen
#  ID: 64010876
#  Exercise: Chapter : 1 - item : 2 - if-elif
# ---------------------------------------------------------
print(' *** Wind classification ***')

temptext = input('Enter wind speed (km/h) : ')
wind_speed = float(temptext)
#print(wind_speed)     # for debugging

classified_string = ''
if wind_speed >= 209.00:
    classified_string = 'Super Typhoon'
elif wind_speed > 102.0 and wind_speed <= 208.99:
    classified_string = 'Typhoon'
elif wind_speed > 56.00 and wind_speed <= 101.99:
    classified_string = 'Tropical Storm'
elif wind_speed > 52.00 and wind_speed <= 55.99:
    classified_string = 'Depression'
elif wind_speed > 0.00 and wind_speed <= 51.99:
    classified_string = 'Breeze'

classified_string = classified_string.strip()
print('Wind classification is', classified_string, end =".")

