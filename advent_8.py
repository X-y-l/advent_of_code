import numpy as np

tree_grid = np.zeros((99,99))
vis_trees = np.zeros((99,99))
scenic_scores = np.zeros((99,99))

with open('advent_8_text.txt') as f:
    text = f.readlines()
    for x in range(99):
        for y in range(99):
            tree_grid[x][y] = text[x][y]

for i in range(4):
    for y in range(len(tree_grid)):
        current_tree_height = -1
        for x in range(len(tree_grid[0])):
            tree = tree_grid[y][x]
            if tree > current_tree_height:
                current_tree_height = tree
                vis_trees[y][x] = 1

    tree_grid = np.rot90(tree_grid)
    vis_trees = np.rot90(vis_trees)


for y in range(99):
    for x in range(99):
        current_score = 1
        for i in range(x-1,-1,-1):
            if tree_grid[y][i] >= tree_grid[y][x] or i == 0:
                current_score *= x-i
                break

        for i in range(y-1,-1,-1):
            if tree_grid[i][x] >= tree_grid[y][x] or i == 0:
                current_score *= y-i
                break

        for i in range(x+1,99):
            if tree_grid[y][i] >= tree_grid[y][x] or i == 98:
                current_score *= i-x
                break

        for i in range(y+1,99):
            if tree_grid[i][x] >= tree_grid[y][x] or i == 98:
                current_score *= i-y
                break
        
        scenic_scores[y][x] = current_score

print(np.sum(vis_trees))
print(np.amax(scenic_scores))