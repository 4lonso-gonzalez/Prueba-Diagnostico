#1. Los pilares de la programación orientada a objetos consisten en herencia, polimorfismo, abstracción y encapsulamiento.
#2. Una clase consiste en un conjunto de metodos los cuales son capaces de ser heredados.
#3. Un objeto es un espacio en la memoria, el cual se le puede asignar un valor o caracter.

from Profesion import Profesion

def PreguntarNombre():
    return input("\nIngrese su nombre: ")

def PreguntarEdad():
    return int(input("\nIngrese su edad: "))

def PreguntarSexo():
    print("\nSELECCIONE SU GENERO: ")
    print("1. Masculino \n2. Femenino")
    return int(input("Seleccion: "))

def PreguntarProfesion():
    print("\nSELECCIONE SU PROFESIÓN: ")
    print("1.Ingeniero \n2.Abogado \n3.Otra")
    return int(input("Seleccion: "))

def PreguntarSueldo():
    return int(input("\nIngrese su sueldo: "))

def CalcularPorcentaje(numero_profesionales, numero_total):
    return (numero_profesionales/numero_total) * 100

def main():
    abogados = []
    ingenieros = []
    otros = []

    while True:
        nombre = PreguntarNombre()

        edad = PreguntarEdad()
        while (edad <= 0):
            print("Edad invalida, vuelva a ingresar.")
            edad = PreguntarEdad()

        sexo = PreguntarSexo()
        while (sexo != 1 and sexo != 2):
            print("Seleccion invalida, vuelva a ingresar")
            sexo = PreguntarSexo()

        profesion = PreguntarProfesion()
        while (profesion != 1 and profesion != 2 and profesion != 3):
            print("Seleccion invalida, vuelva a ingresar")
            profesion = PreguntarProfesion()

        sueldo = PreguntarSueldo()
        while (sueldo <= 0):
            print("Sueldo invalido")
            sueldo = PreguntarSueldo()

        if (profesion == 1):
            nuevoIngeniero = Profesion(nombre, sueldo, len(ingenieros))
            ingenieros.append(nuevoIngeniero)
            for ingeniero in (ingenieros):
                ingeniero.SumarPersona()

        elif (profesion == 2):
            nuevoAbogado = Profesion(nombre, sueldo, len(abogados))
            abogados.append(nuevoAbogado)
            for abogado in (abogados):
                abogado.SumarPersona()

        else:
            nuevoOtro = Profesion(nombre, sueldo, len(otros))
            otros.append(nuevoOtro)
            for otro in (otros):
                otro.SumarPersona()
        
        check = input("\n¿Quiere seguir añadiendo personas?: ")
        if (check != "Si"):
            break

    totalPersonas = len(ingenieros) + len(abogados) + len(otros)
    totalIngenieros = 0
    totalAbogados = 0
    totalOtros = 0

    for ingeniero in ingenieros:
        totalIngenieros += ingeniero.GetSueldo()

    for abogado in abogados:
        totalAbogados += abogado.GetSueldo()

    for otro in otros:
        totalOtros += otro.GetSueldo()
    
    totalSueldos = totalAbogados + totalIngenieros + totalOtros

    def promedioIngenieros():
        if len(ingenieros) != 0:
            return totalSueldos / len(ingenieros)
        else:
            return 0
    
    def promedioAbogados():
        if len(abogados) != 0:
            return totalSueldos / len(abogados)
        else:
            return 0
    
    def promedioOtros():
        if len(otros) != 0:
            return totalSueldos / len(otros)
        else:
            return 0

    porcentajeIngenieros = CalcularPorcentaje(len(ingenieros), totalPersonas)
    porcentajeAbogados = CalcularPorcentaje(len(abogados), totalPersonas)
    porcentajeOtros = CalcularPorcentaje(len(otros), totalPersonas)

    print(f"\nPorcentaje de ingenieros: {porcentajeIngenieros}%")
    print(f"Sueldo promedio de ingenieros: {promedioIngenieros()} CLP")
    
    print(f"\nPorcentaje de abogados: {porcentajeAbogados}%")
    print(f"Sueldo promedio abogados: {promedioAbogados()} CLP")

    print(f"\nPorcentaje de otros: {porcentajeOtros}%")
    print(f"Sueldo promedio de otros {promedioOtros()} CLP")

main()