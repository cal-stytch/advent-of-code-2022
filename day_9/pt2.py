from collections import namedtuple
fn = 'input.txt'
# fn = 'test.txt'
contents = open(fn).read().split('\n')

Move = namedtuple('MOVE', ['dir', 'val'])

moves = [Move(x.split()[0],int(x.split()[1])) for x in contents]

KNOTS = 10
curr_rope = [(0,0) for _ in range(KNOTS)]

def perform_move(move: Move, rope):
    for _ in range(move.val):
        rope = perform_submove(move.dir, rope)
    return rope

def perform_submove(direction, rope):
    # Move the head and then all following knots
    x = 0
    y = 0
    match direction:
        case 'U':
            y = 1
        case 'D':
            y = -1
        case 'L':
            x = -1
        case 'R':
            x = 1
        case _:
            raise Exception()
    new_head = (rope[0][0] + x, rope[0][1] + y)
    rope[0] = new_head

    for i in range(1, KNOTS):
        ith_knot = adjust_to_parent_move(rope[i], rope[i-1])
        rope[i] = ith_knot

    last_knot_loc.add(rope[-1])
    return rope

def adjust_to_parent_move(instance, parent):
    if abs(instance[0] - parent[0]) <= 1 and abs(instance[1] - parent[1]) <=1:
        return instance

    # Horizontal movement
    if (instance[1] == parent[1] and instance[0] != parent[0]):
        if (instance[0] < parent[0]):
            return (parent[0] -1, parent[1])
        else:
            return (parent[0] +1, parent[1])
    # Vertical movement
    if (instance[0] == parent[0] and instance[1] != parent[1]):
        if (instance[1] < parent[1]):
            return (parent[0], parent[1]-1)
        else:
            return (parent[0], parent[1]+1)
    
    # Diagonal movement
    if abs(instance[0] - parent[0]) > abs(instance[1] - parent[1]):
        if (instance[0] < parent[0]):
            return (parent[0] - 1, parent[1])
        else:
            return (parent[0] + 1, parent[1]) 
    
    if abs(instance[0] - parent[0]) < abs(instance[1] - parent[1]):
        if (instance[1] < parent[1]):
            return (parent[0], parent[1] - 1)
        else:
            return (parent[0], parent[1]+1)
    
    # Double diagonal!!!
    if abs(instance[0] - parent[0]) == abs(instance[1] - parent[1]):
        if (instance[0] < parent[0] and instance[1] < parent[1]):
            return (parent[0] - 1, parent[1] - 1)
        elif (instance[0] > parent[0] and instance[1] < parent[1]):
            return (parent[0] + 1, parent[1] - 1)
        elif (instance[0] < parent[0] and instance[1] > parent[1]):
            return (parent[0] - 1, parent[1] + 1)
        elif (instance[0] > parent[0] and instance[1] > parent[1]):
            return (parent[0] + 1, parent[1] + 1)



    raise Exception(f"self {instance} par {parent}")

    # Return a tuple that moves according to parents new position
last_knot_loc = set()
last_knot_loc.add(curr_rope[-1])
for m in moves:
    curr_rope = perform_move(m, curr_rope)

print(len(last_knot_loc))