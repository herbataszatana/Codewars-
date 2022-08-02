#Introduction

#There is a war and nobody knows - the #alphabet war!
#There are two groups of hostile letters. #The tension between left side letters and #right side letters was too high and the war #began.

#Task

#Write a function that accepts fight string #consists of only small letters and return #who wins the fight. When the left side wins #return Left side wins!, when the right side #wins return Right side wins!, in other case #return Let's fight again!.

#The left side letters and their power:

#The left side letters and their power:

# w - 4
# p - 3
# b - 2
# s - 1
#The right side letters and their power:

# m - 4
# q - 3
# d - 2
# z - 1
#The other letters don't have power and are #only victims.

def alphabet_war(fight):
    #your code here
    left= 0
    right= 0
    for letter in fight:
        if letter == 'w':
           left = left + 4
        elif letter == 'p':
           left = left + 3 
        elif letter == 'b':
           left = left + 2
        elif letter == 's':
           left = left + 1
        elif letter == 'm':
           right = right + 4
        elif letter == 'q':
           right = right + 3
        elif letter == 'd':
           right = right + 2 
        elif letter == 'z':
           right = right + 1
        else:
            pass 
     
    if left > right:
        result= 'Left side wins!'
    elif left < right:
        result  = 'Right side wins!'
    else:
        result = 'Let\'s fight again!'
    print (result)
    return result 
    
alphabet_war('pq')