calificacionesAlumnos = []
contador = 0
while contador < 10:
    calificacion = float(input("Ingresa la calificacion del primer alumno"))
    calificacionesAlumnos.append(calificacion)
    contador += 1

total = 0
for calificacion in calificacionesAlumnos:
    total += calificacion

print(
    f"el promedio de la clase fue {sum(calificacionesAlumnos) / len(calificacionesAlumnos)}"
)
