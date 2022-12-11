fn = 'input.txt'
# fn = 'test.txt'
contents = open(fn).read().split('\n')

register = 1
cycle = 1
count = 0
cmd = contents.pop(0)
running = True
row = ''
is_adding = False
while running:
    # print("CYCLE: {cycle}, REG {register}")

    # Draw the pixel
    if (abs(((cycle - 1) % 40) - register) <= 1):
        row += '#'

    else:
        row += '.'
    
    # dump row
    if (cycle % 40 == 0): 
        print(row)
        row = ''


    # Execute the command
    if cmd.split()[0] == 'addx' and is_adding:
        cycle += 1
        register += int(cmd.split()[1])
        is_adding = False
    elif cmd.split()[0] == 'addx' and not is_adding: 
        is_adding = True
        cycle += 1 
    elif cmd == 'noop':
        cycle += 1
    else:
        raise Exception('I DID SOMETHING WRONG')

    # Get the next command?
    if not is_adding:
        try:
            cmd = contents.pop(0)
        except:
            running = False