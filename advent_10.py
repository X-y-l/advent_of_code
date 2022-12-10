with open('advent_10_text.txt') as f:
    x = f.read().split("\n")

sigs = [20 + 40*x for x in range(6)]
total_power = 0

for sig in sigs:
    current_power = 1
    counter = 0
    index = 0
    while counter < sig:

        if x[index] != "noop":
            if counter >= sig-2:
                break
            current_power += int(x[index].split()[1])
            counter += 2
            index += 1

        elif x[index] == "noop":
            counter += 1
            index += 1

    total_power += current_power*sig

print(total_power)

################

screen = list("."*40*6)
cycle = 0
sprite_pos = -39
index = 0
add_num = False

while cycle < len(screen):

    if cycle%40 == 0:
        sprite_pos+=40

    if abs(sprite_pos - cycle) <= 1:
        screen[cycle] = "#"

    if x[index] != "noop":
        if add_num == True:
            sprite_pos += int(x[index].split()[1])
            add_num = False
        else:
            add_num = True
            index -= 1

    index += 1
    cycle += 1

for i in range(6):
    print(''.join(screen[i*40:i*40+40]))