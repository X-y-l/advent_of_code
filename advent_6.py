with open('advent_6_text.txt') as f:
    signal = list(f.read())

print([(x+4,signal[x:x+4]) for x in range(len(signal)-3) if len(signal[x:x+4]) == len(set(signal[x:x+4]))][0])
print([(x+14, signal[x:x+14]) for x in range(len(signal)-13) if len(signal[x:x+14]) == len(set(signal[x:x+14]))][0])