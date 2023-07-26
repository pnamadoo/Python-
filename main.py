import time_calculator as a
dayweek=''
horainicial=input("Hora Inicial: ")
horafinal=input("Hora Final: ")
dayweek=input("Si quieres ingresa el dia")
dw=dayweek.upper()

a.add_time(horainicial,horafinal,dw)
