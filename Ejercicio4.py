from tokenize import Double


print("Introduce tú peso:")
peso=input()
peso= int(peso)
print("Introduce tú altura:")
altura=input()
altura=int(altura)

imc = int(peso/altura)

print(f"Tú indice de masa corporal {imc}")