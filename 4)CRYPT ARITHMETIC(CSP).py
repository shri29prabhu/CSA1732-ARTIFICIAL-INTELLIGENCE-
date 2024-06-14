import itertools

def solve_cryptarithm(words, result):
    letters = set(''.join(words) + result)
    assert len(letters) <= 10, "Too many unique letters"

    for perm in itertools.permutations('0123456789', len(letters)):
        table = str.maketrans(''.join(letters), ''.join(perm))
        translated_words = [word.translate(table) for word in words]
        translated_result = result.translate(table)
        
        if any(word[0] == '0' for word in translated_words + [translated_result]):
            continue
        
        if sum(map(int, translated_words)) == int(translated_result):
            return {letter: digit for letter, digit in zip(letters, perm)}

    return None

words = ['SCOOBY', 'DOOO']
result = 'BLINKS'

solution = solve_cryptarithm(words, result)
if solution:
    print("Solution found:")
    for letter, digit in solution.items():
        print(f"{letter} -> {digit}")
else:
    print("No solution found")
    
OUTPUT
>>> %Run lol.py
Solution found:
L -> 0
I -> 2
K -> 4
S -> 7
N -> 3
D -> 5
Y -> 1
B -> 8
O -> 6
C -> 9
>>> 


