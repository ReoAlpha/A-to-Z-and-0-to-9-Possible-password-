import itertools

digits = '0123456789'
combinations = [''.join(combination) for combination in itertools.product(digits, repeat=4)]

with open('all_combinations_4_digits.txt', 'w') as file:
    for combination in combinations:
        file.write(f'{combination}\n')
