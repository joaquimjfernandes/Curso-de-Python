# >>> Retornando Valores [return] <<<
# ---------------------------------------------------
def somar(a=0, b=0, c=0):
    s = a + b + c
    # print(f'A soma vale {s}')
    return s


# Programa Principal
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Meus Cálculos deram {r1}, {r2}, {r3}')
