q1 = int(input())
q2 = int(input())
V1 = []
V2 = []
for _ in range(q1):
    V1.append(int(input()))
for _ in range(q2):
    V2.append(int(input()))
Vr = []
i = 0
j = 0
while i < q1 and j < q2:
    if V1[i] <= V2[j]:
        Vr.append(V1[i])
        i += 1
    else:
        Vr.append(V2[j])
        j += 1
while i < q1:
    Vr.append(V1[i])
    i += 1
while j < q2:
    Vr.append(V2[j])
    j += 1
for valor in Vr:
    print(valor)
