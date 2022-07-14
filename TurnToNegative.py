#Return Negative 

#In this simple assignment you are given a #number and have to make it negative. But #maybe the number is already negative?


def make_negative( number ):
	if number > 0:
		newNum = number - (number * 2);
		print (newNum);
	else: 
		print(number)
		return number; 

make_negative(0)
