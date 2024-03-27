import re
from functools import reduce
def start(string, slst):
    return string[reduce(lambda x,y: re.search(y,string).span()[0] if re.search(y,string) and re.search(y,string).span()[0] < x else x ,slst,len(string)) ::] if reduce(lambda x,y: re.search(y,string).span()[0] if re.search(y,string) and re.search(y,string).span()[0] < x else x ,slst,len(string)) != len(string) else False

def complement(string):
    return "".join(list(map(lambda x: {"A": "T", "T": "A", "C": "G","G":"C"}.get(x),string)))

def end(string,elst):
    return  [i[0] for i in [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)][:(list(filter(lambda x: x[0] in elst, [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)]))[0][1]) + 1]]  if list(filter(lambda x: x[0] in elst, [(string[:len(string) - (len(string) % 3):][i:i+3],int(i/3)) for i in range(0, len(string[:len(string) - (len(string) % 3):]), 3)])) else None

def check(string):
    return (re.match('^[A|C|G|T]+$', string.upper())).group() if bool(re.match('^[A|C|G|T]+$', string.upper())) else False

def codon(slst, elst):
    return reduce(lambda x,y: False if y in elst else x,slst, True)

def three(lst):
    return reduce(lambda x,y: False if len(y) != 3 else x,lst,True)

def DNA(string,start,end):
     return three(start) and three(end) and codon(start,end) and (check(string) != False)

def box(string):
    return [string,string[::-1],complement(string),complement(string[::-1])]

def protein(string, strt, ed):
    return list(filter(lambda z: z,list(map(lambda y: end(y,ed),list(filter(lambda x: start(x,strt),box(string))))))) if box(string) else False

r1 = ["AAT","GCG"]
r2 = ["ACG","TAG"]
r3 = "ACTAATCGGGGAAAGGGAAAGTAGAAA"

