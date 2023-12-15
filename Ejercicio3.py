n=int(input("Escriba un numero entre 1 y 10: "))
m=int(input("Escriba un numero entre 1 y 10: "))
def leer_lineas(numero, linea):
    import os 
    comprobacion = os.path.isfile("tabla"+ str(numero) + ".txt")
    if comprobacion == True: 
        file=open("tabla"+ str(numero)+ ".txt","r")
        lineas = file.readlines()
        print(lineas[m-1])
    else:
        print("El archivo no existe")
leer_lineas(n,m)