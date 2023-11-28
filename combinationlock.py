# Combination Lock

# Koliko stopinj se mora številčnica obrniti, da se sef odpre?


while True:
    zac, k1, k2, k3 = map(int, input().split())
    if not sum([zac, k1, k2, k3]): # ko za vhodne podatke dobim 4 ničle, izvajane ustavimo
        break
    # izpišemo število stopinj za posamezen testni primer
    print((2*40 + (zac - k1 + 40) % 40 + 40 + (k2 - k1 + 40) % 40 + (k2 - k3 + 40) % 40)*9)
    
    

    
    