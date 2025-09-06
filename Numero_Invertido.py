numero=int(input("ingresa el numero a invertir : "))
numero_orig=numero
invertir=0
numero=abs(numero)
while numero>0:
    invertir=invertir*10 + numero%10
    numero=numero//10
if numero_orig<0:
    invertir=-invertir
print(f"el numero original es: {numero_orig} y el invertido es: {invertir}")