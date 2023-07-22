import time
from nprime import fermat
start = time.time()

#-------------------------------- Char to int

def turn_int(lista):
    string = ''
    for i in range(len(lista)):
        string += lista[i]
    return int(string)

#-------------------------------- Text file with digits

file = open('1.txt')

#-------------------------------- Main digit list

num = list()
digits = 21
num = [x for x in file.read(digits)]

#-------------------------------- Main loop
    
while True:

    a = file.read(1)

#-------------------------------- Find possible palindrome

    while a != num[1]:
        num.pop(0)
        num.append(a)
        a=file.read(1)

    num.pop(0)
    num.append(a)

#-------------------------------- Palindrome test /-Edit acording to number of digits-/

    if num[1]!=num[-2]:continue
    if num[2]!=num[-3]:continue
    if num[3]!=num[-4]:continue
    if num[4]!=num[-5]:continue
    if num[5]!=num[-6]:continue
    if num[6]!=num[-7]:continue
    if num[7]!=num[-8]:continue

#-------------------------------- Register the palindrome
    
    end = time.time()

    if a == '': break    # End of file check

    string_1 = (str(digits) + ' ' + str(turn_int(num)) + ' Time: ' + str((end - start) * 1000)
               + ' pos: ' + str(file.tell()) + '\n')

    palindromes = open('palindromes.txt', 'a')
    palindromes.write(string_1)
    palindromes.close()

#-------------------------------- Bigger palindrome check
    
    pos = file.tell() # Position to return after verification

    count = 1
    while True:

        num2 = list()
        file.seek(pos - digits - count)

        num2 = [x for x in file.read(digits + 2 * count)]

        if num2[0] != num2[-1]: break

        string_1 = (str(digits + 2 * count) + ' ' + str(turn_int(num2)) + ' Time: ' + str((end - start) * 1000)
                   + ' pos: ' + str(file.tell()) + '\n')

        palindromes = open('palindromes.txt', 'a')
        palindromes.write(string_1)
        palindromes.close()

        if fermat(turn_int(num2)): # Primality test

            string_1 = (str(digits + 2 * count) + ' ' + str(turn_int(num2)) + ' Time: ' + str((end - start) * 1000)
                       + ' pos: ' + str(file.tell()) + '\n')

            primes = open('primes.txt', 'a')
            primes.write(string_1)
            primes.close()
            
        count += 1

    file.seek(pos) # Return to position

#--------------------------------   Primality test

    if not int(a) % 2 or a == '5': continue
    if fermat(turn_int(num)):

        string_1 = (str(digits) + ' ' + str(turn_int(num)) + ' Time: ' + str((end - start) * 1000)
                   + ' pos: ' + str(file.tell()) + '\n')

        primes = open('primes.txt', 'a')
        primes.write(string_1)
        primes.close()
