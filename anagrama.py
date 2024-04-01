#transformar a palavra em uma lista
#.sorted
#checar se as listas são iguais 

while True:
    try: 
        N = int(input("coloque o tanto de letras e espaços que a frase tem: "))
        if N > 200 or N < 1:
            raise Exception()
        while True:    
            try:
                A=input("primeira frase: ")
                if len(A) != N:
                    raise Exception()
                B=input('segunda frase: ')
                if len(A) != N:
                    raise Exception()
                listA= list(A)
                listB = list(B)
                break
            except:
                print('O tamanho da frase tem que ser do mesmo tamanho que o numero digitado')  
        break     
    except:
        print('digite apenas números entre 1 e 200.')
    

print(len(listA))
print(len(listB))
listA.sort()
listB.sort()
if listA == listB:
     print('s')
else:
     print('n')
