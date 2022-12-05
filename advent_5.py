import string
lines = open("advent_5_text.txt", "r").readlines()

# constructs the depot
depot = []
for i in range(9):
    depot.append([])

for x in range(9):
    for y in range(0,len(lines[x]), 4):
        if lines[x][y+1] in string.ascii_uppercase:
            depot[int(y/4)].append(lines[x][y+1])


"""for z in range(10,512):
    nums = [int(s) for s in lines[z].split() if s.isdigit()]
    for w in range(nums[0]):
        depot[nums[2]-1] = [depot[nums[1]-1][0]] + depot[nums[2]-1]
        del depot[nums[1]-1][0]"""


for z in range(10,512):
    nums = [int(s) for s in lines[z].split() if s.isdigit()]
    depot[nums[2]-1] = depot[nums[1]-1][:nums[0]] + depot[nums[2]-1]
    del depot[nums[1]-1][:nums[0]]


print(''.join([depot[x][0] for x in range(9)]))