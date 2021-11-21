
###
# 21.11
# Gleb
# Есть проблема с реализацией формулы
###

american_mile = 1609.344
american_gallon = 3.785

def litersna_100km_v_miles_and_gallon(x):
    liters =(100*american_gallon)/(x*american_mile)
    return liters

def milesgl_v_litres_km(y):
    miles = (100*american_gallon)/(y*american_mile)
    return miles


x = int(input('Литры на 100 км в галлоны '))
print(litersna_100km_v_miles_and_gallon(x))

y = int(input(' Галлоны на мили в литры '))
print(milesgl_v_litres_km(y))