segundos_por_minuto = 60
minutos_por_hora = 60
horas_por_dia = 24
dias_por_semana = 7

segundos_por_hora = segundos_por_minuto * minutos_por_hora
segundos_por_dia = segundos_por_hora * horas_por_dia
segundos_por_semana = segundos_por_dia * dias_por_semana

segundos_totales = 1000000

semanas = segundos_totales // segundos_por_semana
segundos_restantes = segundos_totales % segundos_por_semana

dias = segundos_restantes // segundos_por_dia
segundos_restantes = segundos_restantes % segundos_por_dia

horas = segundos_restantes // segundos_por_hora
segundos_restantes = segundos_restantes % segundos_por_hora

minutos = segundos_restantes // segundos_por_minuto
segundos = segundos_restantes % segundos_por_minuto

print(segundos_totales, "segundos =", semanas, "semanas", dias, "días", horas, "horas", minutos, "minutos", segundos, "segundos")