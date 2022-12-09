contents = open('input.txt').read().split('\n')
moves = [[x.split()[0], int(x.split()[1])] for x in contents]

SEGMENTS = 10 
LAST = 9
rope = [(0,0) for r in range(SEGMENTS)]
tail_locations = set()
tail_locations.add(rope[LAST])
t_all = []
t_all.append(rope[LAST])
def update_segment(new_head, curr_tail):
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

    return (x,y)

def perform_move(move, rope):
    # print('----------------')
    # print(tail_locations)
    for i in range(move[1]):
        if (move[0] == 'U'):
            rope[0] = (rope[0][0], rope[0][1] + 1)
        elif (move[0] == 'D'):
            rope[0] = (rope[0][0], rope[0][1] - 1)
        elif (move[0] == 'L'):
            rope[0] = (rope[0][0] - 1, rope[0][1])
        elif (move[0] == 'R'):
            rope[0] = (rope[0][0] + 1, rope[0][1])
    
        for j in range(1, len(rope)):
            rope[j] = update_segment(rope[j-1], rope[j])
            if j == LAST:
                tail_locations.add(rope[LAST])
                if rope[LAST] != t_all[-1]:
                    t_all.append(rope[LAST])
    return rope
    
for move in moves:
    rope = perform_move(move, rope)

print(len(tail_locations))
# print(t_all)
print(len(set(t_all)))
print(rope)

for i in range(len(rope)):
   print((rope[i][0] -9, rope[i][1] +133)) 