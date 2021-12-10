from readfromfile import readfromfile

data = readfromfile('power31.txt')

gammarate = []
epsilonrate = []
rowlength = len(data[0])
gammadecimal = 0
epsilondecimal = 0

#collect status to the length of row, positive is 0, negative is 1
for i in range(rowlength):
    gammarate.append(0)
    epsilonrate.append(0)

#O(rows*columns)
for power in data:
    for col in range(rowlength):
        if (int(power[col]) == 0):
            gammarate[col] += 1
        else:
            gammarate[col] -= 1

for i in range(rowlength):
    #1 wins for gamma, 0 wins for epsilon but no contribution
    if (gammarate[i] < 0):
        gammadecimal += pow(2,(rowlength - i - 1))
    #1 wins for epsilon, 0 no contribution to gamma
    else:
        epsilondecimal += pow(2,(rowlength - i - 1))

print(gammadecimal*epsilondecimal)