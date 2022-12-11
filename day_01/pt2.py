all_elf_count = []
count = 0

with open('input.txt') as f:
    line = f.readline()

    while line:
        if (line == '\n'):
            all_elf_count.append(count)
            count = 0
        else:
            count += int(line)
        
        line = f.readline()

all_elf_count.sort()
print(f'The top 3 calorie count is {all_elf_count[-1] + all_elf_count[-2] + all_elf_count[-3]}')


