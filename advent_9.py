import numpy as np

with open('advent_9_text.txt') as f:
    directions = f.readlines()

visited_coords = np.zeros((1000,1000))
visited_coords[0][0] = 1

rope_length = 10
rope = np.zeros((rope_length,2))

for direction in directions:
    headings = ["U","L","R","D"]
    heading_vects = [np.array([0,1]), np.array([-1,0]), np.array([1,0]), np.array([0,-1])]
    distance = int(direction.split()[1])

    for i in range(distance):
        rope[0] = np.add(rope[0], heading_vects[headings.index(direction[0])])

        for j in range(rope_length-1):
            diff = np.add(rope[j+1], -1*rope[j])

            if max([abs(x) for x in diff]) > 1:
                move = np.array([np.sign(diff[0]), np.sign(diff[1])])
            else:
                move = np.array([0,0])
            
            rope[j+1] = np.add(rope[j+1], -1*move)
        
        visited_coords[int(rope[rope_length-1][0])][int(rope[rope_length-1][1])] = 1

print(np.sum(visited_coords))