A, B = map(eval, input().split())

while B == 0:
    A, B = map(int, input().split())

restoDivisao = abs(A)%abs(B)


print(f"{restoDivisao}")