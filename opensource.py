# Open Source

'''Izpiši: koliko oseb se je prijavilo za posamezen projekt. Če se je kdo prijavil na več kot
en projekt ne upoštevaj nobene od njenih dveh prijav'''



projekti = dict() # slovar projektvo z množicami vpisnih ID-jev za kljuce 
proj = None
vse_prijave = []



while True:
    pod = input()
    if pod == "0":
        break
    if pod == "1":
        
        #projekte razporedimo po stevilu vpisov
        projekti_sz = []
        for k, v in projekti.items():
            projekti_sz.append((k, len(v)))
        
        projekti_sz.sort(key = lambda x: (x[1] * -1, x[0]))
        for el in projekti_sz:
            print(el[0], el[1])
        
        projekti = dict()
        proj = None
        vse_prijave = []
        
    
    else:
        if pod.isupper(): # dobimo nov projekt
            if proj != None: # spisku vseh prijav dodamo prijave k prejšnemu projektu
                vse_prijave += list(projekti[proj])
            proj = pod
            projekti[proj] = set() # nov projekt dodamo k ostalim
        else:
            if pod not in vse_prijave:
                projekti[proj].add(pod) # ime shranimo v trenuten projekt
            else:
                for v in projekti.values(): # ime zbrisemo iz imenika prijav
                    if pod in v:
                        v.remove(pod)