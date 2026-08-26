import math

raio = float(input("Valor do Raio: "))

def tratar_erro():
    if raio < 0:
        return False
    return True

if tratar_erro() == True:
    volume = 4/3 * math.pi * (raio ** 3)
    area = 4 * math.pi * (raio ** 2)    
    print(f"Volume: {volume:.2f}")
    print(f"Área: {area:.2f}")
else:
    print("Não é possivel fazer a conta com raio negativo.")