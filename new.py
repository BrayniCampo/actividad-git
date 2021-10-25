peliculas_mostrar={'After', 'A dos metros de ti', 'Arrastrame el infierno', 'Cruella'}
horarios={"10:00 am     11:30am     1:15pm     4:30pm"}
def insertarPleicula ():
    print("Las películas disponibles ahora son: ", peliculas_mostrar)
    print()
    pregun=input("   ¿Quiere agregar una nueva película?   ")
    if pregun=='si':
        cuantas=int(input("  ¿Cuántas películas desea agregar?  "))
        cont=0
        while cont<cuantas:
            nombre=input("Escriba el nombre de la película que desea agregar ")
            print("QUE LO ESCIRBAAAAAAA")
            print("RUUU RUUU RUUU RUUU EEEH")
            print("Ingrese la hora de la función de ", nombre)
            hora=input("  ")
            horarios.add(hora)
            peliculas_mostrar.add(nombre)
            cont=cont+1
        print("  Su película fue agregada exitiosamente: ")
    else: 
        print("  Si desea ver las películas disponibles, por favor vaya a la opción 2 ")
        print("QUÉ DESEA VER")
        print("OK NO JAJAJAJAJAJJAJAJAJA")
        print("WIII WIII WII WII")

def buscarPeliculas():
    preliculaBuscar=input("  Por favor ingrese la película que desea buscar:   ")
    siEsta=False
    for i in peliculas_mostrar:
        if i==preliculaBuscar:
                print("¡GENIAL. LA PELÍCULA BUSCADA SÍ ESTÁ EN CARTELERA!")
                print("UUUUH SÍ ESTÁ JSJSJSJSJS")
                print("QUÉ COOL QUE ESTÉ WIIII")
                siEsta=True
    if siEsta==False:
        print("Lo sentimos, esta película no esta disponible en cartelera. ")
        print("NO SE ENCUNETRAAAAA")
        print("IS VERY SAD JSJJSJSSJSJSJSJS")
        siEsta=False

def darmecuenta():
    i=0
    while i<=10:
        print("La vida es cool :)")

        
