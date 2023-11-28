# Boiling Vegetables

# Kolikšno je najmanjše število rezov, ki jih moramo narediti,
# da bo razmerje med najlažjim in najtežjim kosom zelenjave
# večje od podanega razmerja.

T, N = map(float, input().split())
kosi = [int(el) for el in input().split()]
kosi2 = kosi.copy()

raz = min(kosi)/max(kosi)
koliko = 0
rezi = [0]*int(N)

def rez(i):
    rezi[i] += 1 # dodamo rez k ustreznemu indexu
    kosi[i] = kosi2[i] / (rezi[i]+1) # spremeni kos ta
    

while raz <= T:
    # izvaja se dokler ne dosežemo želenega razmerja
    rez(kosi.index(max(kosi)))
    raz = min(kosi)/max(kosi)
    
print(sum(rezi))
    

    