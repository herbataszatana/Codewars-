#square every digit

#Welcome. In this kata, you are asked to #square every digit of a number and #concatenate them.

#For example, if we run 9119 through the #function, 811181 will come out, because 92 #is 81 and 12 is 1.

#Note: The function accepts an integer and #returns an integer

def square_digits(num):
    newStr =""
    for x in string:
        newStr= newStr + str(int(x)**2)
    return int(newStr)

    
square_digits(9119)