leva = 0
desna = 1
inf = 10**6

N, K =  [int(el) for el in input().split()]

galerija = []
for _ in range(N):
    # tabela vrst v galeriji, vsaka vrsta vsebuje levo in desno sobo 
    galerija.append([int(el) for el in input().split()])
input()

dp = [[[None, None] for _ in range(N)] for _ in range(K+1)]
# vrednos v dp[k][r][c] predstavlja delno tabelo kjer moramo zapreti
# k sob va tabeli s r vrsticami kjer je v prvi vrstic izbran stolpec c

def f(k, r, c):
    if k == 0:
        # ko sob ne rabimo vec zapreti bo vrednost zaprtih sob 0
        return 0
    if r < 0:
        return inf
    if dp[k][r][c] != None:
        return dp[k][r][c]
        # ce smo vrednost za tako instanco sobe že dobili jo vrnemo
    vrednost_sobe = galerija[r][c]
    dp[k][r][c] = min(f(k-1, r-1, c) + vrednost_sobe, f(k, r-1, leva), f(k, r-1, desna))
    
    return dp[k][r][c]

print(sum(sum(galerija, [])) - min(f(K, N-1, leva), f(K, N-1, desna)))
# od celotne vrednosti galerije odštejemo minimalno vrednost možnih zaprtih sob