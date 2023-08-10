
#inicio de variables
contador_apuesta = 0
acumulador_apuesta = 0
contador_quiniela = 0
contador_quini6 = 0

class   Loteria:
    def _init_(self, num=Nombre):
        self.num = num or random


    def menu():
        global contador_apuesta   
        global acumulador_apuesta
        global contador_Quiniela
        global contador_quini 6

         #monto fijo de la quinela
         #monto_quinela = 400
         #se imprimen los contenidos del menu 
    print(" ")
    print("**************************************")
    print("* quinela    'quini' *")
    print("**************************************")
    print(" ")
    print("1. quiniela")
    print("2. quini 6")
    print("3. probar apuesta")
    print("4. arqueo de caja")
    print("5. salir")
    print(" ")
    print("**************************************")
    print("| precionar boton para continuar |")    
    print("**************************************")
    print(" ")

     seleccion = int(input("ingresar datos: ")):


# cuando el usuario apriete el boton 1, se solicitara que ingrese su apuesta de la quinela 
    if seleccion == 1:
        print("------------------------------------")
        print("quinela - quini")
        print("------------------------------------")
        #input tiket de quini
        nombre = str(input("Ingrese el nombre: "))
        fecha = str(input("Ingrese la fecha: "))
        hora = str(input("Ingrese la hora de la apuesta: "))
        dni = str(input("Ingrese el DNI del apostador: "))

        
        apuesta_quiniela = int(input("ingrese el numero de su apuesta (2, 3 o 4 cifras): "))
        if apuesta_quiniela <10 or apuesta_quiniela >9999:
            print(" ")
            print("ERROR: Ingrese un numero entre 2 y 4 cifras. Vuelva a ingresar los datos de nuevo.")
            print(" ")
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            menu()

             ingresoApuesta = float(input("Ingrese el monto de la apuesta: $ "))

        #IMPRESION TICKET DE LA QUINIELA
        print(" ")
        print("------------------------------------")
        print("quinela - quini")
        print("------------------------------------")
        print(" ")
        print("Cliente: ",nombre,"\nFecha: ",fecha,"\nHora: ",hora,"\nDocumento: ",dni,"\nNumero apostado: ",apuesta_quiniela,"\nMonto apostado: $",ingresoApuesta)
        print(" ")
        print("------------------------------------")
        print(" agradesemos su juego- jugar es perjudicial para la salud  ")
        print(" ")
        print("---------Guarde su ticket-----------")
        print(" ")
        #se contabiliza la apuesta y se carga al acumulador el monto total.
            
   
   

