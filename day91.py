from readfromfile import readfromfile
#test = ['2199943210','3987894921','9856789892','8767896789','9899965678']
test = readfromfile("day91.txt")
increment = 1
total = 0
rows = len(test)-1
cols = len(test[0])-1
topleftcorner = (0,0)
toprightcorner = (0,cols)
bottomleftcorner = (rows,0)
bottomrightcorner = (rows,cols)
topline = lambda a, b : (a == 0) and (b > 0) and (b < cols)
bottomline = lambda a, b : (a == rows) and (b > 0) and (b < cols)
leftside = lambda a, b : (a > 0) and (b == 0) and (b < rows)
rightside = lambda a, b : (b == cols) and (a > 0) and (a < rows)

LEFT = lambda row, col : test[row][col-1] > test[row][col]
RIGHT = lambda row, col : test[row][col+1] > test[row][col]
UP = lambda row, col : test[row-1][col] > test[row][col]
DOWN = lambda row, col : test[row+1][col] > test[row][col]

def checklowpoint(row,col,directions):
    lowscore = 0
    for check in directions:
        if check(row,col):
            lowscore += 1
    if (lowscore == len(directions)):
        print(i,j,test[i][j])
        lowscore = int(test[row][col]) + increment
    else:
        lowscore = 0
    return lowscore

for i in range(rows+1):
    for j in range(cols+1):
        if (i,j) == topleftcorner:
            total += checklowpoint(i,j,[DOWN,RIGHT])
        elif (i,j) == toprightcorner:
            total += checklowpoint(i,j,[DOWN,LEFT])
        elif (i,j) == bottomleftcorner:
            total += checklowpoint(i,j,[UP,RIGHT])
        elif (i,j) == bottomrightcorner:
            total += checklowpoint(i,j,[UP,LEFT])
        elif leftside(i,j):
            total += checklowpoint(i,j,[UP,DOWN,RIGHT])
        elif rightside(i,j):
            total += checklowpoint(i,j,[UP,DOWN,LEFT])
        elif topline(i,j):
            total += checklowpoint(i, j, [RIGHT, DOWN, LEFT])
        elif bottomline(i,j):
            total += checklowpoint(i, j, [RIGHT, UP, LEFT])
        else:
            total += checklowpoint(i, j, [RIGHT, UP, DOWN, LEFT])

print(total)

