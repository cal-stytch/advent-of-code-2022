file_name = 'input.txt'

contents = open(file_name).read()

groups = list(map(lambda e: e.split(',') ,contents.split()))
count = 0

for group in groups:
    a = list(map(int, group[0].split('-'))) 
    b = list(map(int, group[1].split('-')))

    if (a[0] >= b[0] and a[1] <= b[1]) or (b[0] >= a[0] and b[1] <= a[1]):
        count += 1


print(count)