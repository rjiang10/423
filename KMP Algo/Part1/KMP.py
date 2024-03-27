from functools import reduce
f = open("input","r")
o = open("output","w")
base = f.readline().strip()
s = reduce(lambda x,y: x + y,[i.readline().strip() for i in f],"")

t = len(s)
count = t *[0]

i = 1
j = 0

while i < t:
    if s[i] == s[j]:
        # print("MATCH at ",i )
        j += 1
        count[i] = j
    elif j != 0:
        j = count[j-1]
        i -= 1
    i += 1

i = 0
j = 0

while i <= j:
    if s[j] == s[i]:
        j += 1
        i += 1
    if j == t:
        j = count[j-1]
    elif s[j] != s[i] and i < t:
        if j != 0:
            j = count[j-1]
        else:
            i += 1

count = list(map(str,count))
yuh = ' '.join(count)
print(yuh)
o.write(yuh)
o.close()