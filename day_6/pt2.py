
file_name = 'input.txt'
contents = open(file_name).read()

BUFFER_SIZE = 14

buffer = []
for i, c in enumerate(contents):

    buffer.append(c)
    if (len(buffer) > BUFFER_SIZE):
        # drop the first item 
        buffer=buffer[1:]
    
    if (len(buffer) == BUFFER_SIZE and len(set(buffer)) == BUFFER_SIZE):
        # Deal with 0 indexing
        print(i+1)
        break