# lista com max e min
# faz a soma do max e min
# tira o max e min e sobra oq tem 
time = 0
habilidade = []
while True:
     try:
        for i in range(0,4):
            A = int(input("quando de habilidade você tem:"))
            if A >=1000 or A<0:
                print('o número precisa ser entre 0-1000')
            elif i > 0:
                if A < habilidade[i]:
                    print("o número precisa ser maior do que o ultimo número que você digitou")
            else:
                habilidade.append(A)
        break
     except:
         print("você precisa colocar um número")
B = max(habilidade)
C = min(habilidade)
time1 = B+C
habilidade.remove(max(habilidade))
habilidade.remove(min(habilidade))
time2 = sum(habilidade)
difTimes = time1 -time2
print(difTimes)