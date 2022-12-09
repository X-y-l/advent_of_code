# library that handles trees
from anytree import Node, RenderTree

# reads the file, turns each of the lines into elements of an array
with open('advent_7_text.txt') as f:
    terminal_lines = f.readlines()

# creates the root node
home = Node("home")
# makes it the current directory
current_directory = home

# creates the dictionary that will be the running total of how large each file is
dir_dict = {
    str(home): 0
}

# for each line, we only care if it's changing directory, or if its showing a file and it's size in the current directory
for line in terminal_lines:
    if line[:4] == "$ cd":
        # if we want to go back a folder, we just change the current directory to be it's parent
        if line[5:7] == "..":
            current_directory = current_directory.parent
        # if we want to go back to the root directory, we just change the current directory to be the home directory
        elif line[5] == "/":
            current_directory = home
        # otherwise, we want to go into a specific folder, in which case we create a new node on the tree and go into it (and also add it to the dictionary)
        else:
            dir_name = line[5:-1]
            current_directory = Node(dir_name, current_directory)
            dir_dict[str(current_directory)] = 0

    # if the first thing in the line is a number then its a file
    if line.split()[0].isdigit() == True:
        # the first thing is the file size, the second thing is the file name
        file_name = line.split()[1]
        file_size = line.split()[0]
        # adds the file and the file size to the tree
        file = Node(file_name+" "+file_size, current_directory)

        # loops through to the root directory adding the file size to each of the files parent folders
        x = current_directory
        while x != None:
            dir_dict[str(x)] += int(file_size)
            x = x.parent


# prints the directory nicely :)
for pre, fill, node in RenderTree(home):
    print("%s%s" % (pre, node.name))
print("\n")


# sums the file size of each of the folders that are smaller than the threshold, then outputs it
total_bits = 0
for key in dir_dict:
    if dir_dict[key] <= 100000:
        total_bits += dir_dict[key]
print("the total size of all files less than 100000 is",total_bits)


# we need to delete the smallest file that will free up enough space to allow us to download
# how much space we need:
total_space = 40000000
# the minimum file size for a candidate (any file needs to be at least this big for us to have enough space when we delete it):
min_deletion_space = dir_dict[str(home)] - total_space
# we know deleting everything would free up enough space, so thats our current best guess
current_best = str(home)

for key in dir_dict:
    # for each of the folders, if deleting it would free up enough space, and its smaller than our current best guess, then it's our new best guess
    if dir_dict[key] <= dir_dict[current_best] and dir_dict[key] > min_deletion_space:
        current_best = key

# print the file path and the file size
print("the file we should delete is", current_best.split("'")[1], "with a file size of", dir_dict[current_best])