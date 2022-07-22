#My grandfather always predicted how old people would get, and right before he passed away he revealed his secret!
#
#In honor of my grandfather's memory we will write a function using his formula!
#
#Take a list of ages when each of your great-grandparent died.
#   Multiply each number by itself.
#   Add them all together.
#   Take the square root of the result.
#   Divide by two.

#Example
#predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86
#Note: the result should be rounded down to the nearest integer.
import math 
  

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    #Create empty arrays for ages
    together = [age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8]
    #create empy variable that will store sum of multiplied by each other ages
    sum = 0
    #Start loop that will iterate through all ages in 
    for age in together:
        #Multiply each age by each other
        age = age **2
        #Add age to current sum 
        sum = sum + age
    return math.floor(math.sqrt(sum)/2)
    

predict_age(65, 60, 75, 55, 60, 63, 64, 45)

