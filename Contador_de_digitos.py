n=int(input("ingresa un numero entero:"))
num=abs(n)
contador=0
for digitos in str(num):
    contador+=1
print(f"el numero {n} tiene {contador} digitos en total ")
