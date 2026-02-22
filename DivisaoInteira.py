A, B = map(int, input().split())

while B == 0:
    A, B = map(int, input().split())

divisao = abs(A)//abs(B)

if A * B < 0:
    divisao = -divisao


print(divisao)