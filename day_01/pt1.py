
index = 0
count = 0
maxIndex = -1
maxCount = -1

with open('input.txt') as f:
    line = f.readline()

    while line:
        if (line == '\n'):
    
            if count > maxCount:
                maxCount = count
                maxIndex = index
            # Reset values
            index = index + 1
            count = 0
        else:
            count += int(line)
        
        line = f.readline()

print(f'The best Elf is number {maxIndex}. They have {maxCount} calories!')


