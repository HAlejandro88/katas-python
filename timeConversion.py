
import sys 

def timeConversion(s):
    number = ''
    chunks = s.split(':')
    for caracter in chunks[len(chunks) -1 ]:
        if(caracter.isdigit()):
            number += caracter
    if 'AM' in s:
        if int(chunks[0]) == 12:
            return f'00:{chunks[1]}:{number}'
        else:
            return f'{chunks[0]}:{chunks[1]}:{number}'
    else:
        change_hour = int(chunks[0])
        if change_hour == 12:
            return f'{change_hour}:{chunks[1]}:{number}'
        else:
            change_hour = change_hour + 12
            return f'{change_hour}:{chunks[1]}:{number}'    



print(timeConversion('06:40:03AM'))
print(timeConversion('08:28:19PM'))
print(timeConversion('12:30:19PM'))
print(timeConversion('12:45:08AM'))