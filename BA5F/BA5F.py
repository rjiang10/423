def dic():
    B = open("PAM250.txt", "r")
    d = {}
    x = 0
    y = 0
    c = B.readline().strip().split()
    lines = B.readlines()
    for line in lines:
        l = line[1:].strip().split()
        for i in range(len(l)):
            d[c[y] + c[x]] = int(l[i])
            y += 1
        x += 1
        y = 0
    return d

file = open("input", "r")
put = [file.readline().strip().replace(" ", ""), file.readline().strip().replace(" ", "")]
d = dic()

x = put[0]
y = put[1]
br = min(len(x),len(y))
final = [0,0,0]
s1f = ""
s2f = ""

for c in range(br):
  m = len(x)
  n = len(y)
  arr = [[0 for j in range(n + 1)] for i in range(m + 1)]
  contiguous_sum = [[0 for j in range(n + 1)] for i in range(m + 1)]

  for i in range(1, m + 1):
      arr[i][0] = arr[i - 1][0] - 5
      contiguous_sum[i][0] = max(contiguous_sum[i - 1][0] - 5, 0)

  for j in range(1, n + 1):
      arr[0][j] = arr[0][j - 1] - 5
      contiguous_sum[0][j] = max(contiguous_sum[0][j - 1] - 5, 0)


  for i in range(1, m + 1):
      for j in range(1, n + 1):
          score = d.get(x[i - 1] + y[j - 1], 0)
          arr[i][j] = max(arr[i - 1][j] - 5, arr[i][j - 1] - 5, arr[i - 1][j - 1] + score)
          contiguous_sum[i][j] = max(contiguous_sum[i - 1][j] - 5, contiguous_sum[i][j - 1] - 5,
                                      contiguous_sum[i - 1][j - 1] + score, 0)

  i, j = m, n
  s1 = ""
  s2 = ""
  while i > 0 or j > 0:
      if arr[i][j] == arr[i - 1][j - 1] + d.get(x[i - 1] + y[j - 1], 0):
          s1 = x[i - 1] + s1
          s2 = y[j - 1] + s2
          i -= 1
          j -= 1
      elif arr[i][j] == arr[i - 1][j] - 5:
          s1 = x[i - 1] + s1
          s2 = "-" + s2
          i -= 1
      else:
          s1 = "-" + s1
          s2 = y[j - 1] + s2
          j -= 1


  if c == 0:
      s1f,s2f = s1,s2

  for r in range(len(x)):
    for j in range(len(y)):
      if final[0] < contiguous_sum[r][j] or contiguous_sum[r][j] == final[0] and final[2] > max(r,j):
          final = [contiguous_sum[r][j],c,max(r,j)]
  print(final)
  print()
  x = x[1:]
  y = y[1:]

score = final[0]
start = final[1]
end = final[2]
print(s1f[start:end+2],s2f[start:end+2])

o = open("output", "w")
result = "\n".join([str(score),s1f[start:end+2],s2f[start:end+2]])
o.write(result)
o.close()
