#DESCRIPTION:
#Write reverseList function that simply reverses lists.

def reverse_list(lst):
    #Create empty list that will store all items after transfering them into str values
    newList = []
    #Transfer int values into str and add to the newList
    for item in lst:
        str(item)
        newList.append(item)
    #Reverse newList
    newList.reverse()

    return newList



list = [1,2]

reverse_list(list)

