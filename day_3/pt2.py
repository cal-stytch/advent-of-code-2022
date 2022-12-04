file_name = 'i.txt'
# file_name = 'test.txt'

raw_input = open(file_name).read()
raw_sacks = list(map(set, raw_input.split()))

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

# Later updates for learning (able to fully replace for-loop)
f = [raw_sacks[i].intersection(raw_sacks[i+1]).intersection(raw_sacks[i+2]) for i in range(0, len(raw_sacks), 3)]
total_new = sum([score_char(list(g)[0]) for g in f]) 
print(total_new)