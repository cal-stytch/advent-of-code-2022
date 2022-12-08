fn = 'input.txt'
f = open(fn)
contents = f.read()

tree_grid = [[*c]for c in contents.split('\n')]

max_scene_val = 0
# i is the negative Y axis
# j is the positive X axis
for i, row in enumerate(tree_grid):
    for j, val in enumerate(row):
        # Find edges

        scene_val = 0
        if i == 0 or j == 0 or i == len(tree_grid) - 1 or j == len(row) - 1:
            # edges will always have a 0 score. We can ignore
            scene_val = 0
        else:
            def calc_sv(h, arr):
                v = 0
                for a in arr:
                    v += 1
                    if (int(a) >= int(h)):
                        break
                return v

            west = tree_grid[i][:j]
            west.reverse()
            w_sv = calc_sv(tree_grid[i][j], west) 
            east = tree_grid[i][j+1:]
            e_sv = calc_sv(tree_grid[i][j], east) 
            north = [tree_grid[x][j] for x in range(i)]
            north.reverse()
            n_sv = calc_sv(tree_grid[i][j], north) 
            south = [tree_grid[x][j] for x in range(i+1, len(tree_grid))]
            s_sv = calc_sv(tree_grid[i][j], south) 

            scene_val = n_sv * s_sv * e_sv * w_sv
            if(scene_val >= max_scene_val):
                max_scene_val = scene_val
            
print(max_scene_val)