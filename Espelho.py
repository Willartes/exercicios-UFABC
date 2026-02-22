A, B = map(eval, input().split())

A = str(A)
B = str(B)

if A == B[::-1]:
    print("espelho")
else:
    print("nao espelho")