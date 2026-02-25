N = int(input())
G = int(input())
M = int(input())

fatias = G * 8 + M * 6

if fatias > N:
    sobra = fatias - N
else:
    sobra = 0

print(sobra)
