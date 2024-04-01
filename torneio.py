jogos_torneio = 6
resultado = []
vitoria = 0
while jogos_torneio >0:
    jogo = input()
    resultado.append(jogo)
    jogos_torneio -= 1

for resultados in resultado:
    if resultados == 'v':
        vitoria += 1
if vitoria == 0:
    print('-1')
elif vitoria <= 2:
    print('3')
elif 2< vitoria <=4:
    print('2')
else:
    print('1')
    

    