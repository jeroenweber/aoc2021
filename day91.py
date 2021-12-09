test = ['2199943210','3987894921','9856789892','8767896789','9899965678']

lowpointcorner = lambda a , b : (test[a][b+1] > test[a][b]) and (test[a+1][b] > test[a][b])
lowpointtop = lambda a , b : lowpointcorner(a,b) and (test[a][b-1] > test[a][b])
lowpointinline = lambda a, b : lowpointtop(a,b) and (test[a-1][b] > test[a][b])

increment = 1
total = 0
rows = len(test)
cols = len(test[0])
corners = {(0,0),(0,cols-1),(rows-1,0),(rows-1,cols-1)}
topline = lambda a, b : (a == 0) and (b > 0) and (b < cols -1)
bottomline = lambda a, b : (a == rows -1) and (b > 0) and (b < cols -1)
leftside = lambda a, b : (b == 0) and (a > 0) and (a < rows - 1)
rightside = lambda a, b : (a == cols - 1) and (b > 0) and (b < rows - 1)

corner = lambda a, b : (a,b) in corners

print(leftside(1,0))

# for i in range(rows):
#     for j in range(cols):
#         if corner(i,j):
#             if (lowpointcorner(i,j)):
#                 total += test[i,j] + increment
#         elif top(i,j):
#             if (lowpointtop(i,j)):
#                 total += test[i,j] + increment
#         else:
#             if (lowpointinline(i, j)):
#                 total += test[i, j] + increment

print(total)

