# Dirty Driving

vnos1 = input().split(" ")
i = int(vnos1[0])
p = int(vnos1[1])
razdalje = [int(el) for el in input().split(" ")]

razdalje.sort()

moj_t = []
for i in range(len(razdalje)):
    moj_t.append(p * (i + 1) - razdalje[i])
    
    
print(max(moj_t) + razdalje[0])