from functools import reduce
import time
start = time.time()
f = open("input","r")
o = open("output","w")
count = []
base = f.readline().strip()
string = reduce(lambda x,y: x + y,[i.strip() for i in f],"")
check = True

for i in range(len(string)-len(base)+1):
    if string[i] == base[0]:
        for j in range(len(base)):
            if string[i+j] != base[j]:
                check = False
        if check == True:
            count.append(str(i))
        check = True
yuh = ' '.join(count)
print(yuh)
o.write(yuh)
o.close()
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")