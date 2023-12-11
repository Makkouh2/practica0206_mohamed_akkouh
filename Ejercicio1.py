
n=int(input("Escriba un número entero entre el 1 y 10: "))
file="tabla"+ str(n)+ ".txt"
m=open(file,"w")
for i in range (1,11):
    x=n*i
    print(x)
    m.write(str(x) + "\n")