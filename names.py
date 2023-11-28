# Palindrome names

'''glede na podano ime ugotovi koliko najmanj korakov je potrebnih, da
ime spremeniš v palindrom.
Možna koraka sta:
- zamenjava neke črke za drugo
- dodajanje črke na konec'''

ime = input()
#ime = "abcdefgded"
og_ime = ime
dol = len(ime)


def pali(b):
    '''sprejme besedo in vrne koliko crk
    se ne ujema s svojo zrcalno sliko'''
    rev = b[::-1]
    koliko = 0
    for i in range(len(b)//2):
        if b[i] != rev[i]:
            koliko += 1
    return koliko
    
resitve = []
for i in range(dol//2):
    #najvec korakov ki jih potrebujemo do palindroma je (dolzina imena)//2
    #kar pomeni da veckrat kot ((dolzina imena)//2)-1 ne rabimo dodati crke
    resitve.append(i + pali(ime)) #vsaka resitev je seštevek števila dodanih črk na konec
    #in števila črk, ki se ne ujemajo s svojo zrcalno sliko po dodatku
    ime = og_ime + og_ime[:i+1][::-1] 

if len(resitve) == 0: #kadar je podano ime dolžine 1, se zgornja zanka ne izvede in je tabela
                    # 'resitve' prazna, zato ji dodamo ustrezno rešitev.
    resitve.append(0)


print(min(resitve))
    


    
    






