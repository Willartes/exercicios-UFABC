A, B = map(int, input().split())

print(*(i for i in range(A, B + 1) if i % 2 == 0))
print(*(i for i in range(A, B + 1) if i % 2 != 0))