import os

num_pastas = 1000

steps = 10**11

name = 'user'

update = b'sudo apt-get update'
pip = b'sudo apt-get -y install python3-pip'
nprime = b'pip install nprime'
y_cruncher = (b'wget http://www.numberworld.org/y-cruncher/y-cruncher%20v0.7.10.9513-static.tar.xz'
              + b' && sudo apt-get install xz-utils && tar -xvf y-cruncher\ v0.7.10.9513-static.tar.xz'
              + b' && sudo rm y-cruncher\ v0.7.10.9513-static.tar.xz')
down = b'wget https://storage.googleapis.com/pi100t/Pi%20-%20Dec%20-%20Chudnovsky/Pi%20-%20Dec%20-%20Chudnovsky%20-%20'

for i in range(num_pastas):
    string = str(i+1)
    os.mkdir(string)
    
    string2 = './' + string + '/1.sh'
    file = open(string2, 'wb')
    file.write(b'#!/bin/bash\n')
    file.write(update + b' && ' + pip + b' && ' + nprime + b' && ' + y_cruncher)
    file.write(b'\n\n')
    file.write(b'mkdir -p real/')
    
    file.write(string.encode('utf-8'))
    
    file.write(b' && ' + down)
    file.write(str(i).encode('utf-8'))
    file.write(b'.ycd && ')
    file.write(b'sudo mv Pi\ -\ Dec\ -\ Chudnovsky\ -\ ')
    file.write(str(i).encode('utf-8'))
    file.write(b'.ycd ./y-cruncher\ v0.7.10.9513-static && cd y-cruncher\ v0.7.10.9513-static\n')
    file.write(b'./y-cruncher <<finish\n')
    file.write(b'5\n')
    file.write(b'Pi - Dec - Chudnovsky - ')
    file.write(str(i).encode('utf-8'))
    file.write(b'.ycd\n2\n')
    file.write(str(1 + steps * i).encode('utf-8'))
    file.write(b'\n')
    file.write(str((1 + i) * steps).encode('utf-8'))
    file.write(b'\n')
    file.write(b'1.txt\nfinish\n\n')
    file.write(b'sudo mv ')
    file.write(b'1.txt /home/' + name.encode('utf-8') + b'/real/')
    file.write(str(i+1).encode('utf-8'))
    file.write(b' && cd .. && sudo mv ')
    file.write(b'find_prime_palindrome.py ./real/')
    file.write(str(i+1).encode('utf-8'))
    file.write(b'\ncd real/')
    file.write(str(i+1).encode('utf-8'))
    file.write(b' && python3 ')
    file.write(b'find_prime_palindrome.py\n')
    file.write(b'mkdir -p ' + str(i+1).encode('utf-8'))
    file.write(b'\ncp primes.txt palindromes.txt ./' + str(i+1).encode('utf-8'))
    file.close()
