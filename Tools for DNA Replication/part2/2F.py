from functools import reduce


f = open("input","r")
o = open("output","w")
d = {'A':0,'T':0,'G':1,'C':-1,'a':0,'t':0,'g':1,'c':-1}
arr = [0] + [d.get(x) for x in reduce(lambda x,y: x + y,[i.strip() for i in f],"")]
tmn = 0
cmn = 0
r = []
for i in range(len(arr)):
    bruh = arr[i] + cmn

    if bruh < tmn:
        tmn = bruh
        cmn = bruh
        r = [str(i)]
    elif bruh == tmn:
        r.append(str(i))
    cmn = bruh
if len(r) > 1 and r[0] == "0":
     r.remove("0")


yuh = " ".join(r)
print(yuh)
o.write(yuh)
o.close()