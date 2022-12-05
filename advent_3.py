import numpy as np
import string

with open('advent_3_text.txt') as f:
    sacks = f.readlines()

def compartment_calcs(sack):
    compart_size = int(len(sack)/2)
    compart_a = sack[:compart_size]
    compart_b = sack[compart_size:]

    priority_sum = 0

    duplicates = np.intersect1d(compart_a, compart_b)
    for duplicate in duplicates:
        priority_sum += list(string.ascii_letters).index(duplicate)+1

    return priority_sum

total_priorities = 0

for sack in sacks:
    total_priorities += compartment_calcs(list(sack))

print(total_priorities)

##############################################

total_group_priorities = 0
for i in range(0, len(sacks), 3):
    total_group_priorities += 1 + list(string.ascii_letters).index(np.intersect1d(np.intersect1d(list(sacks[i]),list(sacks[i+1])),list(sacks[i+2]))[-1])
print(total_group_priorities)