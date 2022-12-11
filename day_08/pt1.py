fn = 'input.txt'
f = open(fn)
contents = f.read()

tree_grid = [[*c]for c in contents.split('\n')]

count = 0
# i is the negative Y axis
# j is the positive X axis
for i, row in enumerate(tree_grid):
    for j, val in enumerate(row):
        # Find edges
        if i == 0 or j == 0 or i == len(tree_grid) - 1 or j == len(row) - 1:
            count += 1
        else:
            west = tree_grid[i][:j]
            east = tree_grid[i][j+1:]
            north = [tree_grid[x][j] for x in range(i)]
            south = [tree_grid[x][j] for x in range(i+1, len(tree_grid))]

            if (tree_grid[i][j] > min(max(west), max(east), max(north), max(south))):
                count+=1

print(count)