import matplotlib.pyplot as plt
from functools import reduce

def skew_diagram(genome):
    skew = [0]
    score = {"A":0, "T":0, "C":-1, "G":1}
    for base in genome:
        skew.append(score[base] + skew[-1])
    return skew

def find_min_skew(skew):
    min_skew = min(skew)
    min_positions = [i for i, val in enumerate(skew) if val == min_skew]
    return min_positions

f = open("input","r")
genome = reduce(lambda x,y: x + y,[i.strip() for i in f],"")
# Replace 'my_script.py' with your Python file's name
with open('Tools for DNA Replication/part2/1F.py') as file:
    exec(file.read())
skew = skew_diagram(genome)
# Find minimum skew and positions
min_skew = min(skew)
min_positions = [i for i, val in enumerate(skew) if val == min_skew]

# Plot the skew diagram
plt.plot(range(len(skew)), skew)

# Highlight the minimums in red
for min_pos in min_positions:
    plt.plot(min_pos, min_skew, 'ro')

plt.plot(range(len(skew)), skew)
plt.xlabel('Position in Genome')
plt.ylabel('Skew')
plt.title('Skew Diagram')

plt.show()


