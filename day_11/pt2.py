from collections import namedtuple

fn = 'input.txt'
contents = open(fn).read()
raw_monkey =contents.split('\n\n')

Monkey = namedtuple('Monkey', ['items', 'op', 'test', 'count'])
# Starting monkies
monkeys = [
    # 0
    Monkey([56, 56, 92, 65, 71, 61, 79], lambda n: n * 7, lambda n: 3 if  n % 3 == 0 else 7, 0),
    # 1
    Monkey([61, 85], lambda n: n + 5, lambda n: 6 if  n % 11 == 0 else 4 ,0),
    # 2
    Monkey([54, 96, 82, 78, 69], lambda n: n * n, lambda n: 0 if  n % 7 == 0 else 7 ,0),
    # 3
    Monkey([57, 59, 65, 95], lambda n: n + 4, lambda n: 5 if  n % 2 == 0 else 1 ,0),
    # 4
    Monkey([62, 67, 80], lambda n: n * 17, lambda n: 2 if  n % 19 == 0 else 6 ,0),
    # 5
    Monkey([91], lambda n: n + 7, lambda n: 1 if  n % 5 == 0 else 4 ,0),
    # 6
    Monkey([79, 83, 64, 52, 77, 56, 63, 92], lambda n: n + 6, lambda n: 2 if  n % 17 == 0 else 0 ,0),
    # 7
    Monkey([50, 97, 76, 96, 80, 56], lambda n: n + 3, lambda n: 3 if  n % 13 == 0 else 5 ,0)
]


ROUNDS = 10000
tracker = [0 for _ in range(len(monkeys))]
for j in range(ROUNDS):
    for i, monkey in enumerate(monkeys):
        while(len(monkey.items) > 0):
           item = monkey.items.pop(0) 
           tracker[i] = tracker[i] + 1
        # Turns out it is safe to simplify this out by the least common multiple (LCM). I had to look this up.
           new_worry = monkey.op(item) % 9699690

           monkeys[monkey.test(new_worry)].items.append(new_worry)

tracker.sort()
print(tracker[-1] * tracker[-2])