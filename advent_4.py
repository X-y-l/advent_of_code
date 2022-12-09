# reads the file and adds each line to a list (I could've done this a little better by just doing .split("\n") but it doesn't make much of a difference.)
with open('advent_4_text.txt') as f:
    assigns = f.readlines()

# function to determine if one range is entirely contained in another range
def is_overlapping_entire(assignment):
    # list comprehension thing to basically just put the numbers in the right variables and delete extraneous characters
    [[a_start, a_end], [b_start, b_end]] = [[int(y) for y in x.split("-")] for x in assignment.strip("\n").split(",")]
    # the only way they're entirely overlapping is if A is inside B, in which case B starts before A and ends after A, or the other way around.
    return (a_start <= b_start and a_end >= b_end) or (a_start >= b_start and a_end <= b_end)


# function to determine if there is any overlap at all between the two ranges
def is_overlapping(assignment):
    # same as before
    [[a_start, a_end], [b_start, b_end]] = [[int(y) for y in x.split("-")] for x in assignment.strip("\n").split(",")]
    # if A starts before B, then they're overlapping if A ends any time after B starts.
    # if, however, A starts after B starts, then they only overlap if it's also starting before it ends.
    return (a_start <= b_start and a_end >= b_start) or (a_start >= b_start and a_start <= b_end)


# just calculates how many overlap for each of the functions and outputs the answers
num_complete_overlapping = 0
for assignment in assigns:
    num_complete_overlapping += is_overlapping_entire(assignment)
print("There are", num_complete_overlapping, "that have one range completely contained in another.")

num_overlapping = 0
for assignment in assigns:
    num_overlapping += is_overlapping(assignment)
print("There are", num_overlapping, "that have some overlap at all.")