A, B = map(int, input().split())

for i in range(A, B + 1):
    if i == B:
        print(i) 
    else:
        print(i, end=" ") 
