def parse_crate_input(s):
    # Returns Array where index maps to row in input and stores array of crates
    s2 = s.split('\n')
    s3 = []
    for t in s2:
        s3.append([t[x+1] for x in range(0, len(t)-2, 4)])
    # Drop the row number data
    s3.pop()
    s3.reverse()

    crates = [ [] for _ in range(len(s3)+1)]
    
    for row_index, row in enumerate(s3):
        for item_index, item in enumerate(row):
            if (item != ' '):
                crates[item_index].append(item)

    return crates

def parse_move_input(s):
    lines = s.split('\n')
    return [[int(x.split()[1]), int(x.split()[3]), int(x.split()[5])] for x in lines]


def perform_move(crates, move):
    for i in range(move[0]):
        c = crates[move[1]-1].pop() 
        crates[move[2]-1].append(c) 
    return crates 

def print_cargo(cargo):
    for r in cargo:
       print(r) 
    print('---------')

contents = open('input.txt').read()
contents = contents.split('\n\n')
crates = parse_crate_input(contents[0])
moves = parse_move_input(contents[1])

for move in moves:
    crates = perform_move(crates, move)

print(''.join([a[-1] for a in crates]))
