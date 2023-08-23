


def pangrams(s):
    letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j','k','l','m','n','o', 'p','q', 'r','s','t','u', 'v', 'w', 'x', 'y', 'z']
    checkParagrams = []
    num = 0

    for letter in letters:
        if letter in s.lower():
            checkParagrams.append(True)
        else: 
            checkParagrams.append(False)
    
    
    for check in checkParagrams:
        if check == True:
            num += 1
        else:
            num += 0
          

    if num == int(len(checkParagrams)):
        return 'pangram'
    else:
        return 'not pangram'


#print(pangrams('We promptly judged antique ivory buckles for the next prize'))
#print(pangrams('We promptly judged antique ivory buckles for the prize'))