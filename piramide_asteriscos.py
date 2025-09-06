num=int(input("ingresa un numero para la altura de la piramide :"))
for i in range(1,num+1):
    espacios=' '*(num-i)
    asterisco='*' *(2*i-1)
    print(espacios+asterisco)
