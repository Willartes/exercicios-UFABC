P, Q = input().split()

p = (P == "true")
q = (Q == "true")

if p == True:
    p_int = 1
    
else:
    p_int = 0
    

if q == True:
    q_int = 1
else:
    q_int = 0    

soma = p_int + q_int

if soma == 0:
    print("false false")
elif soma == 1:
    print("false true")
else:
    print("true false")   
