def affiche1():
    for i in [0, 3]:
        print(i)

def affiche2():
    for j in [0, 1, 2, 3]:
        print(j)

def affiche3():
    for k in range(3):
        print(k)

def affiche4():
    for m in range(4):
        print(m)


        L = []
for k in range(1, 100):
    L += [k]
print(L)

L = []
for k in range(1, 100):
    L.append(k)
print(L)

L = 100 * [0]
for k in range(1, 100):
    L[k-1] = k
print(L)

for i in range(len(L)):
    L[i] *= 2
print(L)

def carre(n):
    return [i ** 2 for i in range(1, n + 1)]
print(carre(5))

doubles = [2* i for i in range(1, 100)]
print(doubles)

def carre_compr(n):
    return [i**2 for i in range(1, n + 1)]
print(carre_compr(3)) 