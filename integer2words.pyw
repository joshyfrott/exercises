from tkinter import *
import tkinter.messagebox

def affix(string_aff, digit_aff, value_aff):
	post_fix = ""
	lowest = True
	ones_place = 0
	x = 4
	group = [" Thousand,", " Million,", " Billion,", " Trillion,"]
	group_ = 0
	if value_aff != "0": #checks if a postfix is needed
		if digit_aff % 3 == 0:
			post_fix = " Hundred"

		if digit_aff >= x: #determines which group the current digit belongs to
			while ones_place != x:
				if x <= digit_aff <= (x + 2):
					ones_place = x
				else:
					x = x + 3
					group_ = group_ + 1

		while digit_aff > ones_place and lowest == True:
		#checks if the current digit is the 1s place of the group, or if current digit is the lowest value of the group
			lowest = string_aff[(-digit_aff) + 1:(-digit_aff) + 2] == "0"
			digit_aff = digit_aff - 1

		if lowest == True: #checks if there is no postfix added to the current group yet
			post_fix = post_fix + group[group_]
	return post_fix

def converter():
	in_val = ""
	try:
		in_val = int(input_number.get().strip().replace(",",""))
		#filters unnecessary characters, then tries to convert the input to integer
		str_val = str(in_val)
		output_number.set("")

		if in_val <= 999999999999999: #checks if the input is less than trillions
			add_normal = ["", " One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"]
			add_teen = [" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
			add_ty = ["", "", " Twenty", " Thirty", " Fourty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
			digit_count = 1 #starts the digit count
			while len(str_val) + 1 != digit_count: #continues the loop while the digit count does not exceed the input length
				if digit_count == 1: #created because string indexing doesn't allow zero values
					current_number = str_val[-1:]
				else:
					current_number = str_val[-digit_count:(-digit_count)+1] #uses the digit count to assign the current number checked

				if (digit_count -1) % 3 == 0:
				#isolates the 1s, 1 thousands, 1 millions, 1 billions, and 1 trillions
					if str_val[-(digit_count+1):-digit_count] == "1":
					#checks if the 10s', 10 thousands', 10 millions', 10 billions' and 10 trillions' places are 1 
						add_word = add_teen
					else:
						add_word = add_normal
				elif (digit_count -2) % 3 == 0:
				#isolates the 20s, 30s, 40s, 50s, 60s, 70s, 80s, and 90s of 10s', 10 thousands',' 10 millions', 10 billions', and 10 trillions' place
					add_word = add_ty
				else:
					add_word = add_normal

				current_digit = digit_count
				if add_word == add_teen:
					digit_count = digit_count + 2 #skips the next digit
				else:
					digit_count = digit_count + 1
				output_number.set(add_word[int(current_number)] + affix(str_val, current_digit, current_number) + output_number.get())
				
			if output_number.get()[-1:] == ",": #checks and removes trailing comma
				remove_end = output_number.get()
				remove_end = remove_end[:-1].strip()
				output_number.set(remove_end)
		else: #message if the input is more than trillions
			tkinter.messagebox.showerror("Error!", "Input Cannot be Larger than Trillions!")
	except Exception as ex:
		tkinter.messagebox.showerror("Error!", "Invalid Input!\n%s" % ex)
#start of gooey
app = Tk()
app.title("Integer to English Converter")
app.geometry('950x100+200+100')

output_number = StringVar()
output_number.set("")

Label(app, textvariable = output_number).pack()

Label(app, text = "Enter Number to Convert:").pack()
input_number = Entry(app, width = 50)
input_number.pack()

convert = Button(app, text = 'Convert', width = 10, command = converter)
convert.pack(side = 'bottom', padx = 10, pady = 10)

app.mainloop()
