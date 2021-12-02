from readfromfile import readfromfile

data = readfromfile('direction21.txt')
fpos = 0
aim = 0
dpos = 0

for direction in data:
    dirdat = direction.split(' ')
    delta = int(dirdat[1])
    if (dirdat[0] == 'forward'):
        fpos += delta
        dpos += delta*aim
    elif (dirdat[0] == 'up'):
        aim -= delta
    else: #down
        aim += delta
print(fpos*dpos)
