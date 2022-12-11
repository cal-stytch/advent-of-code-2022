with open('i') as f:

    full_text = f.read()

    normalized_text = [[y for y in x.split()] for x in full_text.split('\n')]
    
    opponent = [ord(round[0]) - 64 for round in normalized_text]
    outcome = [round[1] for round in normalized_text]
    rounds = list(zip(opponent, outcome))
    print(rounds)

    def outcome_to_move(o_move, outcome):
        if outcome == 'Y': return o_move

        if outcome == 'Z': return (o_move % 3) + 1
        
        if outcome == 'X' and o_move != 1: return o_move - 1

        else: return 3

    your_moves = [outcome_to_move(r[0], r[1]) for r in rounds]

    print(your_moves)

    def score(opponent, you):
        base = you
        if opponent == you: return base + 3
        
        if you > opponent and you != 3: return base + 6

        if you == 3 and opponent == 2: return base + 6

        if you == 1 and opponent == 3: return base + 6
        
        return base + 0 

    score = sum([score(r[0], r[1]) for r in zip(opponent, your_moves)])

    print(score)
