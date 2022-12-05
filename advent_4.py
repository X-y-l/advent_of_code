with open('advent_4_text.txt') as f:
    assigns = f.readlines()

def is_overlapping_entire(assignment):
    assignment = list(assignment)
    a_start = int("".join(assignment[:assignment.index("-")]))
    del assignment[:assignment.index("-")+1]
    a_end = int("".join(assignment[:assignment.index(",")]))
    del assignment[:assignment.index(",")+1]
    b_start = int("".join(assignment[:assignment.index("-")]))
    del assignment[:assignment.index("-")+1]
    b_end = int("".join(assignment))

    if (a_start <= b_start and a_end >= b_end) or (a_start >= b_start and a_end <= b_end):
        return 1
    return 0

num_overlapping = 0

for assignment in assigns:
    num_overlapping += is_overlapping_entire(assignment)

print(num_overlapping)

######################################

def is_overlapping(assignment):
    assignment = list(assignment)
    a_start = int("".join(assignment[:assignment.index("-")]))
    del assignment[:assignment.index("-")+1]
    a_end = int("".join(assignment[:assignment.index(",")]))
    del assignment[:assignment.index(",")+1]
    b_start = int("".join(assignment[:assignment.index("-")]))
    del assignment[:assignment.index("-")+1]
    b_end = int("".join(assignment))

    if (a_start <= b_start and a_end >= b_start) or (a_start >= b_start and a_start <= b_end):
        return 1
    return 0

num_overlapping_2 = 0

for assignment in assigns:
    num_overlapping_2 += is_overlapping(assignment)

print(num_overlapping_2)