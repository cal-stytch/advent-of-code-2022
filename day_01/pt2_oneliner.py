# Did this code golf after the fact just to remind myself some python tricks for later days

# v1
# print(sum(sorted(map(lambda i: sum(i), map(lambda s: map(lambda n: int(n), s.split()), open('i').read().split('\n\n'))))[-3:]))

# v2    
print(sum(sorted([sum([int(s) for s in t.split()]) for t in open('i').read().split('\n\n')])[-3:]))

# Tip from JK
# print(sum(sorted([sum(map(int,t.split())) for t in open('i').read().split('\n\n')])[-3:]))