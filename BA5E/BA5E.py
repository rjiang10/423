def dic():
    B = open("BLOSUM62.txt","r")
    d = {}
    x = 0
    y = 0
    c = B.readline().strip().split()
    lines = B.readlines()
    for line in lines:
        l = line[1:].strip().split()
        for i in range(len(l)):
            d[c[y]+c[x]] = int(l[i])
            y += 1
        x += 1
        y = 0
    return d

file = open("input","r")
put = [file.readline().strip().replace(" ",""), file.readline().strip().replace(" ","")]
d = dic()
x = put[0]
y = put[1]
m = len(x)
n = len(y)
arr = [[0 for j in range(len(y) + 1)] for i in range(len(x) + 1)]
for i in range(1, len(x) + 1):
    arr[i][0] = arr[i-1][0] - 5
for j in range(1, len(y) + 1):
    arr[0][j] = arr[0][j-1] - 5
for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
      score = d.get(put[0][i-1] + put[1][j-1], 0)
      arr[i][j] = max(arr[i-1][j] - 5, arr[i][j-1] - 5, arr[i-1][j-1] + score)
i = len(x)
j = len(y)
s1 = ""
s2 = ""
while i > 0 or j > 0:
  if arr[i][j] == arr[i-1][j-1] + d.get(put[0][i-1] + put[1][j-1], 0):
    s1 = put[0][i-1] + s1
    s2 = put[1][j-1] + s2
    i -= 1
    j -= 1
  elif arr[i][j] == arr[i-1][j] - 5:
    s1 = put[0][i-1] + s1
    s2 = "-" + s2
    i -= 1
  else:
    s1 = "-" + s1
    s2 = put[1][j-1] + s2
    j -= 1
max_score = arr[m][n]

print(max_score)
print(s1)
print(s2)
o = open("output","w")
yuh = "\n".join([str(max_score),s1,s2])
o.write(yuh)
o.close()