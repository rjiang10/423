f = open("input","r")
n = open("output","w")
Ac = 0
Cc = 0
Gc = 0
Tc = 0
for i in f:
    for j in i:
            if j == "A":
                Ac += 1
            elif j == "C":
                Cc += 1
            elif j == "G":
                Gc += 1
            elif j == "T":
                Tc += 1
txt = "{A:} {C:} {G:} {T:}"
fin = txt.format(A = Ac, C = Cc, G = Gc, T = Tc)
n.write(fin)
n.close()