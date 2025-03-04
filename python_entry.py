# This is the start of the entry level coding stuff for BIT M1 (CS) done by T. van Beelen and A. Capitano
import random
import string

#1
def hello_world_python():
	print("M1BIT: Hello, Python World!")
#2
def hello_world_one_line():
	print("Hello, world, this is a Python def function.\nIt's awesome to make the computer do stuff!")
#3
def fancy_hello_world():
	print("""
    _    ____   ____ ___ ___ 
   / \  / ___| / ___|_ _|_ _|
  / _ \ \___ \| |    | | | | 
 / ___ \ ___) | |___ | | | | 
/_/   \_\____/ \____|___|___|
""")
#4
# Timo: Laatste lijn (de print) is unreachable -> vs code werkt dan toch iets makkelijker dan terminals en standaard text editors
def grade_is_valid(grade):
	if grade >= 1 and grade <= 10:
		return True
	else:
		return False

#5
def test_is_valid(test):
	if isinstance(test,int) and (test >= 1 and test <= 3):
		return True
#6
def is_the_same(message1, message2):
	if isinstance(message1, str) and isinstance(message2, str):
		if message1.casefold() is message2.casefold():
			return True
		else: return False
	return None
#7
def month_name(month_number):
	if isinstance(month_number, int) and (month_number >=1 and month_number <= 12):
		match month_number:
			case 1:
				return "January"
			case 2:
				return "February"
			case 3:
				return "March"
			case 4:
				return "April"
			case 5:
				return "May"
			case 6:
				return "June"
			case 7:
				return "July"
			case 8:
				return "August"
			case 9:
				return "September"
			case 10:
				return "October"
			case 11:
				return "November"
			case 12:
				return "December"
	
	else: print("Invalid argument. The month_number must be an int value between 1 and 12")
	
#8
def sleep_at_home(weekday, vacation):
	if isinstance(weekday,int):
		if (weekday <= 5 and weekday >= 1):
			if vacation == False:
				return True
			else: return False
		elif (weekday <= 7 and weekday >= 6):
			return False
		else: return None
	else: return None

#9 
def format_name(name, surname):
	if not (isinstance(name,str) == True and len(name) >= 2):
		print("inv_name =\"Invalid argument. Name must be string (len>= 2).\"")
		if not (isinstance(surname,str) == True and len(surname) >= 2):
			print("inv_surname =\"Invalid argument. Name must be string (len>= 2).\"")
			return None
		else: return None
	elif not (isinstance(name,str) == True and len(name) >= 2):
		print("inv_surname =\"Invalid argument. Name must be string (len>= 2).\"")
		if not (isinstance(surname,str) == True and len(surname) >= 2):
			print("inv_name =\"Invalid argument. Name must be string (len>= 2).\"")
			return None
		else: return None
	else: x = name(0) + "." + " " + surname + ")" + name + ")"

#10
def calculate_ics_grade(grade_python, grade_oscn, grade_java, test_to_add_bonus, bonus_is_full):
	t1 = grade_python
	t2 = grade_oscn
	t3 = grade_java
	bp = test_to_add_bonus
	if bp == 0:
# not eligible for bonus points; normal calculation
		Final_grade = 0.25*t1 + 0.25*t2 +0.5*t3
		return Final_grade
#bp applied to t1:
	elif bp == 1:
#check if bp can be applied to grade:
		if t1 <=9.5 or t1 >= 5:
#no partial bonus:
			if bonus_is_full == True:
				Final_grade = (0.25*t1+0.5) + 0.25*t2 +0.5*t3
				return Final_grade
#partial bonus:
			else: 
				Final_grade = (0.25*t1+0.25) + 0.25*t2 +0.5*t3
				return Final_grade
# test grade not eligible for bp:
		else: 
			print("Test grade is not eligible to bonus points. Eligible grades are >=5 and <=9.5.")
			return None
#bp applied to t3
	elif bp == 3:
#check if bp can be applied to grade:
		if t3 <=9.5 or t3 >= 5:
#partial bonus cannot be applied to t3:
			if bonus_is_full == False:
				print("Partial bonus points are not allowed in Test 3.")
				return None
#no partial bonus = apply to t3 grade
			else:
				Final_grade = 0.25*t1 + 0.25*t2 +(0.5*t3+0.5)
				return Final_grade
# t3 not eligible for bp:
		else: 
			print("Test grade is not eligible to bonus points. Eligible grades are >=5 and <=9.5.")
			return None
# if bp is not 0, 1 or 3:
	else: print("Invalid argument test_to_add_bonus. Accepted values are 0, 1 or 3.")
	return None
