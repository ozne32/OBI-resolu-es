#quota mensal = X
#numero de meses = N
#quantidade que ele usou M_i
#sobrou = C 
X = int(input("quota:"))
N = (int(input("quantos meses:")))
nX = X
if 1<=X<=100 and 1<=N<=100:
    while N >0:
        M_i = int(input("quanto gastou:"))
        if 0<=M_i<= 1000:
            N -= 1 
            C = nX - M_i
            nX = C + X 
            if M_i> nX:
                print("erro")
            else:
                continue 
        else:
            print("erro")  
    print(nX)  
            
else:
    print("erro")   