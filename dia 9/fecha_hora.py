import datetime
from datetime import datetime
# from datetime import date
#mi_hora = datetime.time(17, 35)
#print(type(mi_hora))
#print(mi_hora.minute)

#mi_fecha = datetime.date(2025, 10, 17)
#print(mi_fecha)
#print(mi_fecha.ctime())

# print(mi_fecha.today())

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime(2022, 10, 5, 23, 45)

vigilia = duerme - despierta
print(vigilia.seconds)

"""
hora_actual = datetime.now()
minutos = hora_actual.minute"""
# mi_fecha = datetime(2015, 5, 15, 22, 10, 15, 2500)
# print(mi_fecha)

# mi_fecha = mi_fecha.replace(month=11)

#nacimiento = date(1995, 3, 3)
#defuncion = date(2095, 6, 19)

#vida = defuncion - nacimiento
#print(vida)
