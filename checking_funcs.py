######################################
###### STANDALONE FUNCTIONS ##########
######################################	
import re 
email_regex = '\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+'
mob_regex = "01[0125][0-9]*"

def check_email(x):      
	if(re.match(email_regex,x)) != None :
		return 1 
	else :
		return 0 
def check_str(x):
	for i in x :
		if i.isdigit() and i != '':
			return  0
	return 1
def check_num(x):
	for i in x :
		if not i.isdigit():
			return  0 
	return 1
def check_mob(x):
	if 	re.match(mob_regex,str(x)) != None :
		return 1 
	else :
		return 0
#########################################
def enter_name():
	while True:
		name = input("Enter student name :")
		if check_str(name) :
			print("Valid Name ")
			break
		else:
			print("Invalid Name ")
	return name 
###########################################
def enter_age():
	while True:
		age = input ("Enter student age :")
		if check_num(age) :
			if int(age) >= 0 and int(age) <= 150 :
				print("Valid age")
				break
			else :
				print("Invalid age")	
		else:
			print("Invalid age")
	return age 
###########################################
def enter_email():	
	while True:
		email = input ("Enter student email :")
		if check_email(email) :
			print("Valid email")
			break
		else:
			print("Invalid email")
	return email
###########################################
def enter_mobile():
	while True:
		mobile = input ("Enter student mobile :")
		if check_num(mobile) : 
			if check_mob(mobile):
				print("Valid mobile")
				break
			else:
				print("Invalid mobile number")
		else :
				print("Invalid  number")
	return mobile
###########################################
def enter_address():
	while True:		
		address = input ("Enter student address :")
		if check_str(address) :
			print("Valid address")
			break
		else:
			print("Invalid address")
	return address
###########################################
###### END OF STANDALONE FUNCS ############
###########################################