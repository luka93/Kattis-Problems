# Succession

'''Ugotovi katera oseba je v najbližjem sorodstvu s kraljem Utopije'''

N, M = [int(el) for el in input().split()]
kralj = input()

tab_sorodstev = [input().split() for _ in range(N)]

tab_kandidatov = [input() for _ in range(M)] 

# imenik vseh imen
vsi = {}
for sorodstvo in tab_sorodstev:
    for el in sorodstvo:
        if el not in vsi:
            vsi.update({el: None})

for el in tab_kandidatov:
    if el not in vsi:
        vsi.update({el: None})
# kralju dodelimo sorodstvo 100% (ali 1)
vsi[kralj] = 1

imenik_sorodstev = {}
for sorodstvo in tab_sorodstev:
    imenik_sorodstev.update({sorodstvo[0]: (sorodstvo[1], sorodstvo[2])})



# funkcija ki sprejme osebo in vrne njen delež kraljeve krvi(sorodstvo)
def sorodstvo(ime):
    
    if vsi[ime] != None:
        return vsi[ime]
    
    if ime not in imenik_sorodstev:
        return 0
    
    return sorodstvo(imenik_sorodstev[ime][0]) * 0.5 + sorodstvo(imenik_sorodstev[ime][1]) * 0.5


kri_kandidatov = [sorodstvo(ime) for ime in tab_kandidatov]

print(tab_kandidatov[kri_kandidatov.index(max(kri_kandidatov))])
        

        