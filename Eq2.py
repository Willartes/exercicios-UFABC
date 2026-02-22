A, B, C = map(eval, input().split())

delta = pow(pow(B, 2) - 4 * A * C, 1/2)

raiz1 = (-B + delta)/(2*A)

raiz2 = (-B - delta)/(2*A)

print(f"{raiz1:.4f} {raiz2:.4f}")
