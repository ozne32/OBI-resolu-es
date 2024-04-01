nmr_arvores = int(input())
lista = []
while nmr_arvores> 0:
    arco = int(input())
    lista.append(arco)
    nmr_arvores -=1 
soma = sum(lista)
print(soma)


