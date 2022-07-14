#Clock shows h hours, m minutes and s #seconds after midnight.
#
#Your task is to write a function which #returns the time since midnight in #milliseconds.

#Input constraints:

#0 <= h <= 23
#0 <= m <= 59
#0 <= s <= 59


def past(h, m, s):
	# Good Luck!
	
   #second is 1000milisevond 
   #minute os 60000 milosexind 
   #hour is 3600000
   hours = h * 3600000
   minutes = m*60000
   sec = s * 1000
   past = hours + minutes +sec
   print(past)
   return past
   
past(0,1,1)
