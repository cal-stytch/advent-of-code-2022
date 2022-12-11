contents = open('input.txt').read().split('\n')
print(contents)
moves = [[x.split()[0], int(x.split()[1])] for x in contents]

head = (0,0)
tail = (0,0)


tail_locations = set()
tail_locations.add(tail)


def get_new_tail(new_head, curr_tail):
    if (abs(new_head[0] - curr_tail[0]) <= 1 and
        abs(new_head[1] - curr_tail[1]) <= 1):
        return curr_tail
    
    x = curr_tail[0]
    y = curr_tail[1]
    if abs(new_head[0] - curr_tail[0]) == 2:
        x = curr_tail[0] + ((new_head[0] - curr_tail[0])//2) 
        if abs(new_head[1] - curr_tail[1]) > 0:
            y = curr_tail[1] + ((new_head[1] - curr_tail[1]))
    
    elif abs(new_head[1] - curr_tail[1]) == 2:
        y = curr_tail[1] + ((new_head[1] - curr_tail[1])//2) 
        if abs(new_head[0] - curr_tail[0]) > 0:
            x = curr_tail[0] + ((new_head[0] - curr_tail[0]))

    tail_locations.add((x,y))
    return (x,y)


for move in moves:
    for i in range(move[1]):
        if (move[0] == 'U'):
            head = (head[0], head[1] + 1)
            tail = get_new_tail(head, tail)
        elif (move[0] == 'D'):
            head = (head[0], head[1] - 1)
            tail = get_new_tail(head, tail) 
        elif (move[0] == 'L'):
            head = (head[0] - 1, head[1])
            tail = get_new_tail(head, tail)
        elif (move[0] == 'R'):
            head = (head[0] + 1, head[1])
            tail = get_new_tail(head, tail)

print(len(tail_locations))