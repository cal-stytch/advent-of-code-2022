file_name = 'input.txt'

contents = open(file_name).read()

groups = list(map(lambda e: e.split(',') ,contents.split()))
count = 0

for group in groups:
    a = list(map(int, group[0].split('-')))
    a_range = set(range(a[0], a[1] + 1))
    b = list(map(int, group[1].split('-')))
    b_range = set(range(b[0], b[1] + 1))
    
    if len(a_range & b_range) > 0:
        count += 1

print(count)
