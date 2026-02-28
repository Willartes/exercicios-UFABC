fib = [0] * 61
fib[0] = 0
fib[1] = 1

i = 2
while i <= 60:
    fib[i] = fib[i - 1] + fib[i - 2]
    i += 1
    
T = int(input())

caso = 0
while caso < T:
    N = int(input())
    print("Fib(" + str(N) + ") = " + str(fib[N]))
    caso += 1
