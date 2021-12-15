rl = ['1163751742','1381373672','2136511328','3694931569','7463417111',
      '1319128137','1359912421','3125421639','1293138521','2311944581']
risklevel = 40

rows = len(rl)
cols = len(rl[0])

tl = [rl[0][0]]
br = [rl[rows-1][cols-1]]

LEFT = lambda row, col : rl[col-1][row] if col > 0 else False
RIGHT = lambda row, col : rl[col+1][row] if col < cols - 1 else False
UP = lambda row, col : rl[col][row-1] if row > 0 else False
DOWN = lambda row, col : rl[col][row+1] if row < rows - 1 else False

print(LEFT(0,0))
print(RIGHT(0,0))