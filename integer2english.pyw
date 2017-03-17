from tkinter import *
import tkinter.messagebox

def affix(string_aff, digit_aff):
#function for appending a postfix
#string_aff is the whole original input in string format
#digit_aff is the current digit checked
	post_fix = "" #variable for the postfix
	lower = True #variable for checking the lower digit

	def check_lower(string_low, digit_low):
	#function for checking if the lower digit is zero
	#string_low is the whole original input in string format
		x = (-digit_low) + 1
		y = (-digit_low) + 2
		#the above 2 variables are used for indexing the lower digit
		if string_low[x:y] == "0": #checks if the lower digit is zero
			check = True
		else:
			check = False
		return check #returns the value to the 'lower' boolean variable inside affix()

	if digit_aff == 3 or digit_aff == 6 or digit_aff == 9 or digit_aff == 12 or digit_aff == 15: #these numbers are the digits of hundreds
		post_fix = " hundred"
	else:
		pass
