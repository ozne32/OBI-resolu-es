# 1 ≤ S ≤ 36
# 1 ≤ A ≤ 10 000
# 1 ≤ B ≤ 10 000
# A ≤ B
S = int(input('valor S: '))
if 1>=S >= 36:
    print(ValueError)
A = int(input('valor A: '))
if 1 >= A >= 10000:
    print(ValueError)

B = int(input('valor B: '))
if 1 <= B <= 10000:
    print(ValueError)
elif A <=B:
    print(ValueError)
C = []
L = []
if A> B:
    C.append(B)
    while A>B:
        C.append(B+1)
        B +=1
elif A<B:
    C.append(A)
    while A<B:
        C.append(A+1)
        A+=1
else:
    C = 0
for num in C:
    numstr = str(num) #precisa transformar o num em string, pois int não é iterável
    soma = sum(int(i) for i in numstr) # para somar os algarismos 
    if soma == S:
        L.append(num)
print(len(L))
    
