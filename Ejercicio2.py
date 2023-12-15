n=int(input("Escriba un número entero entre el 1 y 10: "))
def leer_fichero(numero):
    import os 
    comprobacion = os.path.isfile("tabla"+ str(numero) + ".txt")
    if comprobacion == True: 
        file=open("tabla"+ str(numero)+ ".txt","r")
        tabla = file.read()
        print(tabla)
    else:
        print("El archivo no existe")
leer_fichero(n)