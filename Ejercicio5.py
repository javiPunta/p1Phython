import random
num1= random.randrange(2,10)
num2= random.randrange(2,10)

print(f"{num1}")
print(f"{num2}")


num3 = num1*num2

print("Introduce un número:")
try:
   num4 = int(input())
except Exception as e:
    print(e)
else:
    if num4 == num3:
        print(f"{num3} es igual a {num4}")
    else:
       print(f"{num3} no es igual a {num4}")

      


