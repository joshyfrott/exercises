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

	if digit_aff == 4 or digit_aff == 5 or digit_aff == 6: #these numbers are the three thousand places
		while digit_aff != 4: #while it's not the one thousands places
			lower = check_lower(string_aff, digit_aff) #passes the whole input and the current digit as arguments
			if lower == True:
				digit_aff = digit_aff - 1
			else:
				digit_aff = 4
		post_fix = post_fix + " thousand,"
	elif digit_aff == 7 or digit_aff == 8 or digit_aff == 9: #these numbers are the millions places
		while digit_aff != 7: #while it's not the one millions places
			lower = check_lower(string_aff, digit_aff)
			if lower == True:
				digit_aff = digit_aff - 1
			else:
				digit_aff = 7
		post_fix = post_fix + " million,"
	elif digit_aff == 10 or digit_aff == 11 or digit_aff == 12: #these numbers are the billions places
		while digit_aff != 10: #while it's not the one billions places
			lower = check_lower(string_aff, digit_aff)
			if lower == True:
				digit_aff = digit_aff - 1
			else:
				digit_aff = 10
		post_fix = post_fix + " billion,"
	elif digit_aff == 13 or digit_aff == 14 or digit_aff == 15: #these numbers are the trillions places
		while digit_aff != 13: #while it's not the one trillions places
			lower = check_lower(string_aff, digit_aff)
			if lower == True:
				digit_aff = digit_aff - 1
			else:
				digit_aff = 13
		post_fix = post_fix + " trillion,"

	return post_fix

def normal(string_norm, digit_norm, value_norm):
	add_normal = ""
	if value_norm == "1":
		add_normal = " one"
	elif value_norm == "2":
		add_normal = " two"
	elif value_norm == "3":
		add_normal = " three"
	elif value_norm == "4":
		add_normal = " four"
	elif value_norm == "5":
		add_normal = " five"
	elif value_norm == "6":
		add_normal = " six"
	elif value_norm == "7":
		add_normal = " seven"
	elif value_norm == "8":
		add_normal = " eight"
	elif value_norm == "9":
		add_normal = " nine"
	output_number.set(add_normal + affix(string_norm, digit_norm) + output_number.get())

def teens(string_teens, digit_teen, value_teen):
	add_teen = ""
	if value_teen == "0":
		add_teen = " ten"
	elif value_teen == "1":
		add_teen = " eleven"
	elif value_teen == "2":
		add_teen = " tweleve"
	elif value_teen == "3":
		add_teen = " thirteen"
	elif value_teen == "4":
		add_teen = " fourteen"
	elif value_teen == "5":
		add_teen = " fifteen"
	elif value_teen == "6":
		add_teen = " sixteen"
	elif value_teen == "7":
		add_teen = " seventeen"
	elif value_teen == "8":
		add_teen = " eighteen"
	elif value_teen == "9":
		add_teen = " nineteen"
	output_number.set(add_teen + affix(string_teens, digit_teen) + output_number.get())

def tyty(string_tyty, digit_ty, value_ty):
	add_ty = ""
	if value_ty == "2":
		add_ty = " twenty"
	elif value_ty == "3":
		add_ty = " thirty"
	elif value_ty == "4":
		add_ty = " fourty"
	elif value_ty == "5":
		add_ty = " fifty"
	elif value_ty == "6":
		add_ty = " sixty"
	elif value_ty == "7":
		add_ty = " seventy"
	elif value_ty == "8":
		add_ty = " eighty"
	elif value_ty == "9":
		add_ty = " ninety"
	output_number.set(add_ty + affix(string_tyty, digit_ty) + output_number.get())

def converter():
	in_val = ""
	try:
		in_val = int(input_number.get().strip().replace(",",""))

	except Exception as ex:
		tkinter.messagebox.showerror("Error!", "Invalid Input!\n%s" % ex)
	str_val = str(in_val)
	output_number.set("")
	if in_val <= 999999999999999:
		digit_count = 1
		while len(str_val) + 1 != digit_count:
			if digit_count == 1:
				current_number = str_val[-1:]
			else:
				current_number = str_val[-digit_count:(-digit_count)+1]
			if digit_count == 1 or digit_count == 4 or digit_count == 7 or digit_count == 10 or digit_count == 13:
			#isolates the 1s, 1 thousands, 1 millions, 1 billions, and 1 trillions
				if str_val[-(digit_count+1):-digit_count] == "1":
				#checks if the 10s', 10 thousands', 10 millions',
				#10 billions' and 10 trillions' places are 1 
					teens(str_val, digit_count, current_number)
					digit_count = digit_count + 2 #skips the next digit
				else:
					normal(str_val, digit_count, current_number)
					digit_count = digit_count + 1
			elif digit_count == 2 or digit_count == 5 or digit_count == 8 or digit_count == 11 or digit_count == 14:
			#isolates the 20s, 30s, 40s, 50s, 60s, 70s, 80s, and 90s
			# of 10s', 10 thousands',' 10 millions', 10 billions', and 10 trillions' place
				tyty(str_val, digit_count, current_number)
				digit_count = digit_count + 1
			else:
				normal(str_val, digit_count, current_number)
				digit_count = digit_count + 1
	else:
		tkinter.messagebox.showerror("Error!", "Input Cannot be Larger than Trillions!")
		pass

#start of gooey
app = Tk()
app.title("Mark Kupit's Integer to English Converter")
app.geometry('450x100+200+100')

output_number = StringVar()
output_number.set("")

Label(app, textvariable = output_number).pack()

Label(app, text = "Enter Number to Convert:").pack()
input_number = Entry(app, width = 50)
input_number.pack()

convert = Button(app, text = 'Convert', width = 10, command = converter)
convert.pack(side = 'bottom', padx = 10, pady = 10)

app.mainloop()
