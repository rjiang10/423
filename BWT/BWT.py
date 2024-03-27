def cs(x,y):
    if x[0] == y[0]:
        return -1 if int(x[1:]) < int(y[1:]) else 1
    else:
        return -1 if int(x[0]) < int(y[0]) else 1


from functools import reduce
f = open("input","r")
b = list(reduce(lambda x,y: x + y,[i.strip() for i in f],""))
r = {}

for i in range(len(b)):
    x = b[i] 
    if b[i] in r:
        r[x] = r[x] + 1
        b[i] = (x,r[x])
    else:
       r[x] = 0
       b[i] = (x,0)
z = len(list(zip(sorted(b),b)))
y = dict(zip(sorted(b),b))
c = ("$",0)
d = "$"
for g in range(z):
        print(c,"&",y[c])
        t = y[c]
        d += t[0]
        c = t

o = open("output","w")
yuh = (d[:len(d)-1:])[::-1]
print(yuh)
o.write(yuh)
o.close()