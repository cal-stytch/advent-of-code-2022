file_name = 'i.txt'
# file_name = 'test.txt'

raw_input = open(file_name).read()
raw_sacks = raw_input.split()

def process_sack(raw_sack):
    comp_length = len(raw_sack) // 2
    return set(raw_sack[0:comp_length]).intersection(set(raw_sack[comp_length:]))

def score_char(c):
    if ord(c) >= ord('A') and ord(c) <= ord('Z'):
        return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1 

sacks = list(map(process_sack, raw_sacks))
pri_sum = sum([score_char(list(i)[0]) for i in sacks])
print(pri_sum)
