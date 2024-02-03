# A-to-Z-and-0-to-9-Possible-password-
you can use this wordlist for password cracking and subdomain bruteforcing.This wordlist containing  all the possible passwords.

Here is python code

import itertools

====> 
    #add you want characters or symbols in this this charecter section
    
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    #you want choose your digit which you want ex:repeat=2,repeat=5,repeat=8
    
    combinations = [''.join(combination) for combination in itertools.product(characters, repeat=8)]
    
    #change file name if want. 
    
    with open('all_combinations_8_characters.txt', 'w') as file:
    
    for combination in combinations:
        file.write(f'{combination}\n') 
        
                                      <=====
enjoy
