import itertools

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
combinations = [''.join(combination) for combination in itertools.product(characters, repeat=4)]

with open('all_combinations_4_characters.txt', 'w') as file:
    for combination in combinations:
        file.write(f'{combination}\n')
