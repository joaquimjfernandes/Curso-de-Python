# >>> Retornando Valores [return] <<<
# ---------------------------------------------------
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


# Programa Principal
num = int(input('Digite um número: '))
if par(num):
    print('É Par!')
else:
    print('Não é Par!')
