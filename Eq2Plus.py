import math
A, B, C = map(eval, input().split())

delta = (pow(B, 2) - 4 * A * C)

if delta < 0:
   print("nao ha raiz real") 
else:
   delta = math.sqrt(delta)

   raiz1 = (-B + delta)/(2*A)
   raiz2 = (-B - delta)/(2*A)
   if raiz1 != raiz2:
    print(f"{raiz1:.4f} {raiz2:.4f}")
   else:
     print(f"{raiz1:.4f}") 