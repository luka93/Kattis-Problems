# Pivot

'''v podani vrsti števil, najdi tista katerih vsi predhodniki so manjši(ali enaki) in
naslednjiki večji od števila'''

n = int(input())

s =[int(el) for el in input().split(" ")]

# za vsako število v tabeli s, najdemo tisto število, ki je največje levo od števila
# in ga dodelimo na isto mesto v tabeli levo
levo = [-(2**31) for _ in range(n)]

for i in range(1, n):
    levo[i] = max(levo[i-1], s[i-1])
# za vsako število v tabeli s najdemo tisto število, ki je najmanjšte deso od števila    
desno = [2**31 for _ in range(n)]

for i in range(n-2, -1, -1):
    desno[i] = min(desno[i+1], s[i+1])

# Za vsako število v tabeli s preverimo ali je večje ali enako največjemu
# levo od sebe in manjše od najmanjšega desno od sebe
koliko = 0
for i in range(n):
    if s[i] >= levo[i] and s[i] < desno[i]:
        koliko += 1

print(koliko)