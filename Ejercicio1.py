n=int(input("Escriba un número entero entre el 1 y 10: "))
def multipicacion(n):
    """Función para relizar una multiplicación

    parametros:
    -n=numero entero

    salida:
    -tabla de la multiplicación de dicho numero.
    """
if n<=10 and n>0:
    file="tabla"+ str(n)+ ".txt"
    m=open(file,"w")
    for i in range (1,11):
        x=n*i
        print(x)
        m.write(str(x) + "\n")
else:
    print("No se cumple")
    
multipicacion (n)
