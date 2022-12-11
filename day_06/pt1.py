
file_name = 'input.txt'
contents = open(file_name).read()

buffer = []
for i, c in enumerate(contents):

    buffer.append(c)
    if (len(buffer) > 4):
        # drop the first item 
        buffer=buffer[1:]
    
    if (len(buffer) == 4 and len(set(buffer)) == 4):
        # Deal with 0 indexing
        print(i+1)
        break