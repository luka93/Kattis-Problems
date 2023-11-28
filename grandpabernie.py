# Grandpa Bernie



st_izletov = int(input())

seznam_izletov = []
for i in range(st_izletov):
    seznam_izletov += [input().split(" ")]
#seznam_izletov = [int(el[1]) for el in seznam_izletov]


st_poizvedb = int(input())

seznam_poizvedb = []
for i in range(st_poizvedb):
    seznam_poizvedb += [input().split(" ")]
    

imenik_izletov = {}

for el in seznam_izletov:
    imenik_izletov.update({el[0]: []})

for el in seznam_izletov:
    imenik_izletov[el[0]] += [int(el[1])]
    
for t in imenik_izletov:
    imenik_izletov[t].sort()
    
    
for el in seznam_poizvedb:
    print(imenik_izletov[el[0]][int(el[1]) - 1])