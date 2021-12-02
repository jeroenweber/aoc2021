from readfromfile import readfromfile

data = readfromfile('puzzle11.txt')
prev = int(data[0])
data.pop(0)
increases = 0
total = 1
for depth in data:
    depth = int(depth)
    if depth > prev:
        increases += 1
    prev = depth
    total += 1
print("increases\t" + str(increases))
print("total\t\t" + str(total))