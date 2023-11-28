# Traveling Monk


a, d = [int(el) for el in input().split()]

# za vsak odsek poti v tabelo shranimo tuple ki predstavlja funkcijo visine v odvisnosti od casa vsakega odseka
odseki_vzpon = [] 
s_vzpon = 0 # prehojena višina pri vzponu
t_vzpon = 0 # pretecen cas pri vzponu
for _ in range(a):
    s, t = [int(el) for el in input().split()] # sprememba v visini in pretecen cas v posameznem odseku poti
    f = (s/t, (s/t) * -t_vzpon + s_vzpon, (t_vzpon, t+t_vzpon))
    # f predstavlja funkcijo vsakega odseka poti. Prvi element je koeficient, drugi je prosti clen, tretji
    # pa je par ki oznacuje interval odseka
    odseki_vzpon.append(f)
    t_vzpon += t
    s_vzpon += s

# isto naredimo za spust
odseki_spust = []
s_spust = s_vzpon
t_spust = 0
for _ in range(d):
    s, t = [int(el) for el in input().split()]
    f = (-s/t, (-s/t) * -t_spust + s_spust, (t_spust, t+t_spust))
    odseki_spust.append(f)
    t_spust += t
    s_spust -= s
    
def srecanje():
    # vrne prvo presecisce funkcij vzpona in spusta 
    for f1 in odseki_vzpon:
        for f2 in odseki_spust:
            if f1[0] != f2[0]:
                presek = (f2[1] - f1[1]) / (f1[0] - f2[0])
                if presek <= f1[2][1] and presek <= f2[2][1] and presek >= f1[2][0] and presek >= f2[2][0]:
                    return presek
            
print(srecanje())
        
