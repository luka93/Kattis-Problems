# Postal Delivery

''' Kolikšna je najmanjša razdalja, ki jo mora prepotovati poštar,
da dostavi vsa pisma. '''

N, K = [int(el) for el in input().split()] # stevilo destinacij in kapaciteta



levo = []
desno = []
# Tabeli parov razdalje in kolicine pisem za dostavo
for _ in range(N):
    raz, kol = [int(el) for el in input().split()]
    if raz < 0:
        levo += [(-raz, kol)]
    else:
        desno += [(raz,kol)]

levo = levo[::-1]



def stran(K, pari):
    '''prepotovana razdlalja v eno stran od izhodisca, v eno smer'''
    pot = 0 # Pot v eno smer
    if pari == []:
        return 0
    raz, kol = pari.pop()
    while True:
        pot += raz * (kol // K)
        kol %= K # število preostalih pisem na lokaciji
        if pari == []: # ce ni vec destinacij
            return pot + (raz if kol > 0 else 0) # zadnja vožnja
        if kol == 0: # ce ni vec pisem za dostavo na lokaciji, obravnavamo naslednjo lokacijo
            raz, kol = pari.pop()
            continue
        
        while len(pari) > 0  and kol <= K: # dokler so kolicine pisem za dostavo manjše od kapacitete, jih obravnavamo kot ena dostava
            raz2, kol2 = pari.pop()
            kol += kol2
        
        pot += raz
        kol = kol - K  
        raz = raz2



print((stran(K, levo) + stran(K, desno)) * 2) # seštejemo levo in desno prepotovano pot in upoštevamo tudi povratno pot do postaje