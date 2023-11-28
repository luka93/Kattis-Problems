# Reseto


N, K = [int(el) for el in input().split()]

je_pra = [True] * (N+1)
je_pra[0], je_pra[1] = False, False



def reseto():
    precrtani = 0
    for i in range(2, N+1):
        if not je_pra[i]: # spustimo števila ki smo že precrtali
            continue
        
        for j in range(i, N+1, i):
            if not je_pra[j]: # spustimo vse veckratnike stevila i ki smo jih že precrtali
                continue
            
            je_pra[j] = False 
            precrtani += 1 
            # vsakic ko stevilo precrtamo se prasamo ce smo jiz ze dovolj
            if precrtani == K:
                return j
            

print(reseto())
            
