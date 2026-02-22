N = int(input())

while N > 0:

    M1, M2 = map(eval, input().split())

    if M2 <= 2:
        print("Nova")
    elif M2 >= 97:
        print("Cheia")
    elif M1 < M2:
        print("Crescente")
    else:
        print("Minguante")
    
    N -= 1