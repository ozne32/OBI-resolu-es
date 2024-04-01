# 1 ≤ N ≤ 100 000
# 0 ≤ Xi ≤ 100, para (1 ≤ i ≤ N) número inteiro a ser somado 
# 0 ≤ resultado ≤ 1 000 000
while True:
    try:
        n= int(input('quantos número: '))
        if 1> n  or n >100000:
            raise Exception()
        else:
            listNum = []
            while n>0:
                a = int(input('coloque o número: '))
                if 0>a or a >100:
                    print('o número precisa ser entre 0 e 100')
                else:
                    n -=1
                    if a == 0:
                        listNum.pop()
                    else:
                        listNum.append(a)
            break
    except:
        print('coloque um número entre 1 e 100 000')
while n>0:
    a = int(input('coloque o número: '))
    n -=1
    if a == 0:
        listNum.pop()
    else:
        listNum.append(a)
soma = sum(listNum)
print(soma)