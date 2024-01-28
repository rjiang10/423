import re
from functools import reduce

#checks for start
def start(string, slst):
    return string[reduce(min,list(filter(lambda x: x != None, list(map(lambda x: None if re.search(x,string) == None else (re.search(x,string).span())[0],slst)))))::]

# flips it
def complement(string):
    return "".join(list(map(lambda x: {"A": "T", "T": "A", "C": "G","G":"C"}.get(x),string)))

# 
def end(string,elst):
    return  [i[0] for i in [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)][:(list(filter(lambda x: x[0] in elst, [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)]))[0][1]) + 1]]  if list(filter(lambda x: x[0] in elst, [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)])) else None

print(complement("ACGTACGTAGCC"))
#remember to capitalize the string before doing shit to it
#remember to check if its a valid string
#start cant equal end
print(end("PEELOLIeee",["LOL","MMD"]))