# 1.a própria consoante (vamos chamar de consoante original);
# 2.a vogal mais próxima da consoante original no alfabeto, com a regra adicional de que se a 
# consoante original está à mesma distância de duas vogais, então a vogal mais próxima do início do 
# alfabeto é usada. Por exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois esta 
# é a vogal mais próxima; se a consoante original é c, a vogal que deve ser utilizada é a, porque c está à 
# mesma distância de a e e, e a é mais próxima do início do alfabeto.
# 3.a consoante que segue a consoante original, na ordem do início ao fim do alfabeto. Por exemplo, se a 
# consoante original é d, a consoante a ser utilizada é f. No caso de a consoante original ser z, deve ser 
# utilizada a própria letra z.
alfabeto = "bcdfghjklmnpqrstvxz"
alfabetoL = list(alfabeto)
alfabeto1 = "abcdefghijklmnopqrstuvxz"
vogais = 'aeiou'
P = input('coloque a frase a ser codificada:')
palavra = ''
for letras in P:
    for letras2 in alfabeto:

        if letras == letras2: #vê se é consoante
            primeira_letra = letras[0] #pega a consoante original
            palavra += primeira_letra#adiciona na palavra

            index = alfabeto1.index(letras2) #para pegar o indíce da letra dentro do alfabeto
            if index<=2:
                segunda_letra = 'a'
            elif 3<=index<=6:
                segunda_letra = 'e'
            elif 6<=index<=11:
                segunda_letra = 'i'
            elif 11<=index<18:
                segunda_letra ='o'
            else:
                segunda_letra = 'u'
            palavra += segunda_letra

            for i in range(0, len(alfabetoL)): #checa um por um da lista do alfabetoL
                if letras == alfabetoL[i]: #quando a letra insirida for igual a alguma que está no alfabeto 
                    terceira_letra = alfabetoL[i+1] 
                    # pega a proxima consoante do alfabeto, com base em uma lista sem consoante
                    palavra += terceira_letra
                    if terceira_letra =='z':
                        terceira_letra =='z'
                        palavra += terceira_letra

    for letras3 in vogais:
        if letras == letras3: # vê se é vogal
            letra_vogal = letras3
            palavra += letra_vogal
print(palavra)
            
        