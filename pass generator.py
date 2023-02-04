#PIN generatour
import random 
lower_case = "absdefghijklmnopqrstuvwxyx"
upper_case = "ABSDEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symboles = "#<>=-+*/^%$!?_"
use_for = lower_case + upper_case + number + symboles
while True :
	length_for_pass = input("chouse long password from 1 to 78\n")
	length_for_pass = int(length_for_pass)
	password = "".join(random.sample(use_for, length_for_pass))
	print("************PIN generatour************")
	print(password)