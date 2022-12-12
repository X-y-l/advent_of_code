import math
with open('advent_11_text.txt') as f:
    instructions = f.read().split("\n\n")

new = 0
num_monkeys = len(instructions)
monkey_items = [[int(i) for i in instructions[x].split("\n")[1][18:].split(",")] for x in range(num_monkeys)]
monkey_worry_increase = [instructions[x].split("\n")[2][13:] for x in range(num_monkeys)]
monkey_tests = [int(instructions[x].split("\n")[3][20:]) for x in range(num_monkeys)]
monkey_targets = [[int(instructions[x].split("\n")[i][-1]) for i in [5,4]] for x in range(num_monkeys)]
num_inspected = [0]*num_monkeys

# PART 1:
"""
num_rounds = 20
for i in range(num_rounds):
    for j in range(num_monkeys):
        num_inspected[j] += len(monkey_items[j])
        for old in monkey_items[j]:
            exec(monkey_worry_increase[j])
            current_item = new // 3
            monkey_items[monkey_targets[j][current_item % monkey_tests[j] == 0]].append(current_item)
        monkey_items[j] = []

num_inspected.sort(reverse=True)
print(num_inspected[0] * num_inspected[1])
"""

# PART 2:

num_rounds = 10000
lcm = 1
for i in monkey_tests:
    lcm = lcm*i//math.gcd(lcm, i)

for i in range(num_rounds):
    for j in range(num_monkeys):
        num_inspected[j] += len(monkey_items[j])
        for old in monkey_items[j]:
            exec(monkey_worry_increase[j])
            current_item = new % lcm
            monkey_items[monkey_targets[j][current_item % monkey_tests[j] == 0]].append(current_item)
        monkey_items[j] = []
num_inspected.sort(reverse=True)
print(num_inspected[0] * num_inspected[1])