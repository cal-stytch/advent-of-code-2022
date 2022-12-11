fn = 'input.txt'
# fn = 'test.txt'
contents = open(fn).read().split('\n')

register = 1
cycle = 1
count = 0
for c in contents:
    # print(f'{cycle} {register}')

    if (cycle == 20 or cycle % 40 == 20):
        count += cycle * register

    if c == 'noop':
        cycle += 1
    
    else:
        add_op = c.split()
        print(add_op)
        cycle += 1
        # Check
        if (cycle == 20 or cycle % 40 == 20):
            count += cycle * register
        cycle += 1
        register += int(add_op[1])

print(count)
    

