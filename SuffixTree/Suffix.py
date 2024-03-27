from functools import reduce
f = open("input","r")
bruh = []
class Node:
    def __init__(self,p = None):
        self.p = p
        self.d = dict()
   
  
def shove(n,s):
    if s:
        if s[0] in n.d:
            shove(n.d.get(s[0]),s[1:])
        else:
            while s:
                n.d[s[0]] = Node(s[0])
                n = n.d[s[0]]
                s = s[1:]

def tree(n,s):
    if n:
        z = n.p if n.p else ""
        x = len(n.d.values())
        if x > 1:
            for i in n.d.values():
                tree(i,"")
            bruh.append(s + n.p) if n.p else None
        elif x == 1:
            for i in n.d.values():
                tree(i,s+z)
        else:
            bruh.append(s+n.p)

root = Node()
s = reduce(lambda x,y: x + y,[i.strip() for i in f],"")
for i in range(len(s)):
    t = s[i:]
    shove(root,t)
tree(root,"")
o = open("output","w")
yuh = '\n'.join(bruh)
print(yuh)
o.write(yuh)
o.close()
