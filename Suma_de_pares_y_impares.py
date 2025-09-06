num=int(input("ingresa un numero : "))
sum_pares=0
sum_impares=0

for i in range(1,num+1):
    if i%2==0:
        sum_pares +=i
    else:
        sum_impares+=i
print(f"la suma de los pares es {sum_pares}")
print(f"la suma de los impares es {sum_impares}")