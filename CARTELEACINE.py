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
            print("Ingrese la hora de la función de ", nombre)
            hora=input("  ")
            horarios.add(hora)
            peliculas_mostrar.add(nombre)
            cont=cont+1
        print("  Su película fue agregada exitiosamente: ")
    else: 
        print("  Si desea ver las películas disponibles, por favor vaya a la opción 2 ")
        menu()
def listaPeliculas ():
    if len(peliculas_mostrar)==4 and len(horarios)==4:
        print("La cartelera está conformada de la siguiente manera: ")
        print()
        print("////////////  HORA DE LA FUNCIÓN  ////////////  ")
        print(horarios)
        print(peliculas_mostrar)
    else: 
        print("La cartelera está conformada de la siguiente manera: ")
        print()
        print("////////////  HORA DE LA FUNCIÓN  ////////////  ")
        print(horarios) #AGREGAR EN UN SET
        print(peliculas_mostrar)
def buscarPeliculas():
    preliculaBuscar=input("  Por favor ingrese la película que desea buscar:   ")
    siEsta=False
    for i in peliculas_mostrar:
        if i==preliculaBuscar:
                print("¡GENIAL. LA PELÍCULA BUSCADA SÍ ESTÁ EN CARTELERA!")
                siEsta=True
    if siEsta==False:
        print("Lo sentimos, esta película no esta disponible en cartelera. ")
        siEsta=False
def limpiarPeliculas():
    print("")
    pregun=input("¿ESTÁ SEGURO QUE DESEA ELIMINAR TODAS LAS PELÍCULAS DE LA CARTELERA? ")
    if pregun=='si':
        peliculas_mostrar.clear()
        horarios.clear()
        print("Se ha eliminado con éxito todas las películas. ")
def eliminarPelicula():
    print("Escoja el nombre de la película que desea eliminar ")
    peldelete=input()
    ho=input("Escoga la hora de función que desea eliminar ")
    #CON IF IN PELICULAS_ CON .REMOVE(PELICULASELIMINAR)
    if ho in horarios:
        horarios.remove(ho)
        print("El horario de función ", ho, "fue eliminado exitosamente. ")
    else: 
        print("Este horario no se ha establecido. ")
    if peldelete in peliculas_mostrar:
        peliculas_mostrar.remove(peldelete)
        print("La película ", peldelete, 'fue eliminada exitosamente. ')
    else: 
        print("Lo sentimos, esta película no está disponible en cartelera. ")
def menu():
    si_no=True
    while si_no==True:
        print("")
        print("         ┆┆┆┆┆┆BIENVENIDO A LA CARTELERA DE NUESTRO CINE EL MUNDO ES BELLO┆┆┆┆┆┆     ")
        print("")

        print("Tiene 6 opciones las cuales son:  ")
        print("    Opción 1= Insertar/Agregar una película. ")
        print("    Opción 2= Listar/Observar la cartelera. ")
        print("    Opción 3= Buscar/Corrobar si está disponible una película. ") 
        print("    Opción 4= Eliminar una o varias películas. ")
        print("    Opción 5= Eliminar todas las películas. ") 
        print("    Opción 6= Volver al menú. ") 
        print("    Opción 7= Salir del sistema. ")

        deci=int(input("Por favor escogar el número de la opción que desea ejecutar:  "))
    

        if deci==1:
            si_no==False
            insertarPleicula()
        elif deci==2:
            si_no==False
            listaPeliculas()
        elif deci==3:
            si_no==False
            buscarPeliculas()
        elif deci==4:
            si_no==False
            eliminarPelicula()
        elif deci==5:
            si_no==False
            limpiarPeliculas()
        elif deci==6:
            si_no==False
            menu()
        elif deci==7:

            pregunta=input("Está seguro que desea salir del sistema? ")
            if pregunta=='si' or pregunta=='yes' or pregunta=='Si':
                print(" Muchas gracias por visitar nuestro cine EL MUNDO ES BELLO ")
                si_no==True
                quit()
            else: 
                si_no==False
                menu()
        else:
            print()
            print("Lo sentimos, este número de opción no lo reconoce el sistema. ")
            print()
            si_no==False
            menu() 
menu()             





    


