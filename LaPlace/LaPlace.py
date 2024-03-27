import re
def mtrx(x):
    m = [{'A': 1, 'C': 1,'G': 1,'T': 1} for i in range(k)]
    for i in range(len(x)):
        if (x[i] == 'A' or x[i] == 'C' or x[i] == 'G' or x[i] == 'T'):
            m[i][x[i]] =  m[i][x[i]] + 1
    return m

def mp(m,a):
    count = 0
    for x in str_lst:
            print(a) 
            total = (None,-1)
            for i in range(len(x)-k+1):
                z = x[i:i+k]
                c = 0
                for j in range(k): 
                    c += m[j][z[j]]
                if c > total[1]:
                    total = (z,c)
            count += total[1]
            c = total[0]

            for i in range(k):
                m[i][c[i]] = m[i][c[i]] + 1
            a.append(c)
    return (a,count)

def comp(x,y):
    count = 0
    for i in y:
        for j in range(k):
            if (x[j] == i[j]):
                count += 1
    print(count)
    return count


file = open("input","r")
var_line = re.findall('(\d+)\s+(\d+)',file.readline())
k = int(var_line[0][0])
t = int(var_line[0][1])
first_line = file.readline().strip()
str_lst =[i.strip() for i in file]
l = len(first_line)-k+1
final = (None,-1)
for i in range(l):
    kmer = first_line[i:i+k]
    print(kmer)
    temp_m = mtrx(kmer)
    temp_arr = [kmer]
    x = mp(temp_m,temp_arr)
    y = comp(kmer,temp_arr) 
    if y > final[1]:
        final = (temp_arr,y)
print("Final",final[0])
o = open("output","w")
yuh = '\n'.join(final[0])
o.write(yuh)
o.close()