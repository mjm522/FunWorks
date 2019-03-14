import re

string = '000001110100010'

print(re.findall('10*1', string))

flag3 = lambda x : 3 if x%3 == 0 else None
flag5 = lambda x : 5 if x%5 == 0 else None
flagC = lambda x, y : 'Fizz' if (x and not y) #else ( 'Buzz' if y and not x else ('FizzBuzz' if x and y))
flagc = lambda x:{'Fizz':3, 'Buzz':5, 'FizzBuzz':35}.get(x, ' ')

for i in range(12):

    print(flagC(flag3(i), flag5(i)))
