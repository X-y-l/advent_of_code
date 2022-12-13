# import libararies, numpy for the nice fast arrays, and pyplot from matplotlib to draw a nice grid of colours for us :)
import numpy as np
import matplotlib.pyplot as plt

# if you want the program to do part 1, set part1 = True. If you want it to do part 2, set it = False
part1 = True
part2 = not part1

# opens the file with the data and adds each line to an array
with open('advent_12_text.txt') as f:
    char_grid = f.read().split("\n")

# This file is for testing, I write the distances as an integer to each cell
distances_file = open("advent_12_image.txt", "w")

# initializes a few variables - width and height are the dimensions of our data, grid will be the data converted to numbers, and dist_grid will be a grid of
# distances to each cell
width, height = len(char_grid[0]), len(char_grid)
grid = np.zeros((height, width))
dist_grid = np.zeros((height, width))

# fills grid with the relevant data by looping through each character in the data and setting it to be the correct number in the corresponding cell in grid
for y in range(len(char_grid)):
    for x in range(len(char_grid[0])):
        # if it's the start, we set it = 1
        if char_grid[y][x] == "S":
            grid[y][x] = 1
            # and make note of it's coordinate
            y_0, x_0 = y, x

        # if its the end, we set it = 28 (since a-z will be 2-27, and this is the highest mountain)
        elif char_grid[y][x] == "E":
            grid[y][x] = 28
            # and also save its coords to constants
            y_end, x_end = y, x

        # otherwise we convert the letter to the relevant number and put it in the grid
        else:
            grid[y][x] = ord(char_grid[y][x])-95


# This section creates new_cells, which is relevant to the next part. For now, its just an array filled with tuples representing the coordinates of the starting squares.
new_cells = []

# In part 1, we only start from S, so the only starting point is the (x_0, y_0) we chose earlier
if part1:
    new_cells = [(x_0, y_0)]

# In part 2, we can start from any point that's an a, ie has height 2, or the start. So we just need to check if the relevant grid height is either 1 or 2, then add the
# coords to the list.
if part2:
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] in [1,2]:
                new_cells.append((x,y))


# in this section, i do a kind of flood fill algorithm to determine how long it takes to reach each square in the grid
# initialize variables / constants
finished = False
adjacent = [(1,0), (0,1), (-1,0), (0,-1)]
temp_new = []
depth = 0

# until every cell has been reached, keep going
while not finished:
    # for each of the cells that we had previously just reached
    for cell in new_cells:
        # check each of the adjacent cells
        for vect in adjacent:
            x, y = cell[0]+vect[0], cell[1]+vect[1]

            # if the cell isn't outside of the grid
            if min(x,y) >= 0 and x < width and y < height:
                # if it hasn't already been assigned a value, and it can be reached (it's no greater than 1 taller than the previous cell)
                if dist_grid[y][x] == 0 and grid[y][x] <= grid[cell[1]][cell[0]] + 1:
                    # then we can reach it with distance depth, so add it to the list that will become the new cells next step and set it's distance in dist_grid
                    temp_new.append((cell[0]+vect[0], cell[1]+vect[1]))
                    dist_grid[y][x] = depth

    # if we didnt reach any new cells, then we never will - so the grid is complete.
    if new_cells == []:
        finished = True
    
    # the cells we just reached will become the new cells to go through and check the adjacent ones of, and we need to clear the temporary list and increase the depth
    new_cells = temp_new            
    temp_new = []
    depth += 1


# finally we just need to output our calculations
# for testing, I write the depths to "advent_12_image.txt" so I can see that everything's correct
for line in dist_grid:
    for num in line:
        # pads the number with spaces to be 4 characters, so they all fit nicely in a grid
        distances_file.write("{:4}".format(int(num)))
    distances_file.write("\n")
distances_file.close()

# prints the distance to the finish (obviously)
print(f"The distance to the finish is {int(dist_grid[y_end][x_end]+1)}")

# draws the data in a pcolor grid - the colour gradient "terrain" makes it look like sea and land with a mountain which is really cool so I chose that
plt.figure(figsize=(width/10,height/10))
plt.pcolor(dist_grid, edgecolors='k', linewidths=1, cmap="terrain")
plt.show()