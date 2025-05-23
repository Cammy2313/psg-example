segundos_totales = 1000000

semanas = segundos_totales // (7 * 24 * 60 * 60)
segundos_restantes = segundos_totales % (7 * 24 * 60 * 60)

dias = segundos_restantes // (24 * 60 * 60)
segundos_restantes = segundos_restantes % (24 * 60 * 60)

horas = segundos_restantes // (60 * 60)
segundos_restantes = segundos_restantes % (60 * 60)

minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(segundos_totales, " = ",semanas, "semanas", dias, "días", horas, "horas", minutos, "minutos", segundos, "segundos")