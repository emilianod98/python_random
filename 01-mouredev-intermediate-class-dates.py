#Importamos el modulo de Datetime
from datetime import datetime
#Creamos una variable que guarde la fecha y hora actual
now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


timestamps = now.timestamp()

print(timestamps)


year_2025 = datetime(2025, 4, 25)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(year_2025)
print("#####################################################################")


from datetime import time


current_time = time(21, 6, 40)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)