#exercise 4:
def repete_caractere(c, n):
    return c * n
print(repete_caractere('a', 5))  # Affiche 'aaaaa'
#exercise 5:
def repete_deux_caracteres(c, n, d, m):
    return c * n + d * m

print(repete_deux_caracteres('a', 3, 'b', 4))  
#exercise 6:
def affiche_n_lignes(ch, n):
    for _ in range(n):
        print(ch)

affiche_n_lignes('Bonjour', 3)
def affiche_n_lignes_numerote(ch, n):
    for i in range(1, n + 1):
        print(f"{i}. {ch}")

affiche_n_lignes_numerote('Bonjour', 3)
#exercise 7:
def triangle_caractere(c, n):
    for i in range(1, n + 1):
        print(c * i)

triangle_caractere('*', 4)
#exercise 8:
def premiere_occ(ch, c):
    for i, char in enumerate(ch):
        if char == c:
            return i
    return None

print(premiere_occ('aabcada', 'a'))  
print(premiere_occ('abcd', 'e'))    
#exercise 9:
def nb_occurrence(ch, c):
    return ch.count(c)

print(nb_occurrence('aabcada', 'a'))  
print(nb_occurrence('abcd', 'e'))     
#exercise 10:
def sous_chaine(ch1, ch2):
    return ch1 in ch2 or ch2 in ch1

print(sous_chaine('abc', 'abcd'))  
print(sous_chaine('abc', 'xyz'))  
#exercise 11:
ch = ''
for k in range(1, 5):
    if k % 2 == 1:
        ch += 'a'
    else:
        ch += 'b'
print(ch)

ch = ''
for k in range(4):
    if k % 2 == 1:
        ch += 'a'
    else:
        ch += 'b'
print(ch)
#exercise 12:
def triple_six(ch):
    return '666' in ch

print(triple_six('12366645')) 

def triple_six_exact(ch):
    n = len(ch)
    if ch[:3] == '666' and ch[3] != '6':
        return True
    if ch[-3:] == '666' and ch[-4] != '6':
        return True
    for k in range(1, n - 3):
        if ch[k:k+3] == '666' and ch[k-1] != '6' and ch[k+3] != '6':
            return True
    return False
#exercise 13:
def palindrome(ch):
    return ch == ch[::-1]

print(palindrome('kayak')) 
#exercise 19:
def indices(ch, c):
    return [i for i, char in enumerate(ch) if char == c]

print(indices('abbacccaa', 'a')) 
#exercise 20:
def sous_liste(L1, L2):
    n, m = len(L1), len(L2)
    for i in range(n - m + 1):
        if L1[i:i + m] == L2:
            return True
    return False

print(sous_liste([1, 2, 3, 4, 5], [3, 4])) 
#exercise 21:
def tous_positifs(L):
    return all(x >= 0 for x in L)

print(tous_positifs([1, 2, 3, 0]))  
print(tous_positifs([-1, 2, 3]))  
#exercise 22:
def positifs(L):
    return sum(1 for x in L if x >= 0)

print(positifs([2, -1, 3, 4, -6, 0, 6]))  
def rangs_negatifs(L):
    return [i for i, x in enumerate(L) if x < 0]

print(rangs_negatifs([2, -1, 3, 4, -6, 0, 6])) 
def motif(L):
    return [0, 0] in [L[i:i+2] for i in range(len(L) - 1)]

print(motif([1, 0, 0, 2]))
def dix_vingt(L):
    return all(10 <= x <= 20 for x in L)

print(dix_vingt([15, 12, 20]))  
#exercise 23:
def croissante(L):
    n = len(L)
    for k in range(n - 1):
        if L[k] > L[k + 1]:
            return False
    return True

def monotone(L):
    return croissante(L) or croissante(L[::-1])

print(monotone([1, 2, 3]))   
print(monotone([3, 2, 1]))  
#exercise 25:
def suite(n):
    u = 1
    L = [u]
    for i in range(1, n):
        u = u ** 2 + i
        L.append(u)
    return L

print(suite(5))  
#exercise 26:
def valeur_absolue_liste(L):
    for i in range(len(L)):
        L[i] = abs(L[i])

L = [-1, -2, 3]
valeur_absolue_liste(L)
print(L)  
#exercise 27:
def E_et_sigma(X, P):
    E = sum(x * p for x, p in zip(X, P))
    variance = sum(p * (x - E) ** 2 for x, p in zip(X, P))
    sigma = variance ** 0.5
    return E, sigma

print(E_et_sigma([1, 2, 3], [0.2, 0.5, 0.3]))
#exercise 30:
import copy
M = [[0, 0, 0] for _ in range(3)]
N = copy.deepcopy(M)
#exercise 32:
from copy import deepcopy

def valeur_absolue_liste_2(L):
    return [abs(e) for e in L]
#exercise 33:
def ajout(L, o):
    return L + [o]

def suppr(L, o):
    return [e for e in L if e != o]
