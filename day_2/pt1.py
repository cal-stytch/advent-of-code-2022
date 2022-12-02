with open('i') as f:

    full_text = f.read()

    normalized_text = [[(ord(y))  for y in x.split()] for x in full_text.split('\n')]
    
    opponent = [round[0] - 64 for round in normalized_text]
    you = [round[1] - 87 for round in normalized_text]
    rounds = list(zip(opponent, you))

    def score(opponent: int, you: int):
        base = you
        if opponent == you: return base + 3
        
        if you > opponent and you != 3: return base + 6

        if you == 3 and opponent == 2: return base + 6

        if you == 1 and opponent == 3: return base + 6
        
        return base + 0 

    score = sum([score(r[0], r[1]) for r in rounds])

    print(score)
