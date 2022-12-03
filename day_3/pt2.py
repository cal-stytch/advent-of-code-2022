file_name = 'i.txt'
# file_name = 'test.txt'

raw_input = open(file_name).read()
raw_sacks = raw_input.split()

def score_char(c):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1 

# Split sacks into groups of three and find overlap via sets
groups = []
group = []
for sack in raw_sacks:
    if (len(group) == 3):
        overlap = group[0].intersection(group[1].intersection(group[2]))
        groups.append(overlap)
        group = []
    group.append(set(sack))
# Handle last set after for-loop ends
overlap = group[0].intersection(group[1].intersection(group[2]))
groups.append(overlap)
    
total = sum([score_char(list(g)[0]) for g in groups])
print(total)
