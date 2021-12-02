from readfromfile import readfromfile

def sum(a,b,c):
    return a + b + c

data = readfromfile('puzzle11.txt')
increases = 0
next = True
prevtriple = sum(int(data[0]),int(data[1]),int(data[2]))
data.pop(0)

while next:
    if (data == []):
        next = False
        break
    else:
        if len(data) >= 3:
            nexttriple = sum(int(data[0]),int(data[1]),int(data[2]))
            data.pop(0)
        else:
            data = []
        if nexttriple > prevtriple:
            increases += 1
        prevtriple = nexttriple


print(increases)


