P, Q = input().split()

p = (P == "true")
q = (Q == "true")

if (p and not q) or (not p and q):
    print("true")
else:
    print("false")   
