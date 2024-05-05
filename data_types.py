import math
# String data type 

#literal assignment
first = 'Dave'
last = 'Gray' 

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# # constructor function 
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation 
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)

# casting a number to a string 
decade = str(1980)
# print(type(decade))
print(decade)

statement = "I Like rock music from the " + decade + "s."
print(statement)

# Multiple Lines
multiline = '''
Hey, how are you?

I was just checking in. 

                        All good? 



'''
print(multiline)

# Escaping special characters
sentence = "I\'m back at work!\tHey!\n\nWhere\'s this at\\located?"
print(sentence)

# String Methods 

# print("")
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                                            "
# multiline = "                                     " + multiline 
# print(len(multiline))

# strip whitespace from multiline 
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

print("")

# Build a menu 
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + '$1'.rjust(4))
# print("Muffin".ljust(16, ".") + '$1'.rjust(4))
# print("Bacon".ljust(16, ".") + '$1'.rjust(4))

print("")
# string index values 
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# some methods return boolean data 
print(first.startswith("D"))
print(first.endswith("Z"))
print("")

#boolean data type 
myvalue = True 
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

#numeric data types 
print("")
price = 100 
best_price = int(8)
print(type(price))
print(isinstance(best_price, int))
print("")

#float interger 
gpa = 3.28
y = float(1.14)
print(type(gpa))
print("")

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print("")

# Built-in functions for numbers 

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))



print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number 
zipcode = "10475"
zip_value = int(zipcode)
print(type(zip_value))
print(zip_value)

#error if you attempt to cast incorrect data 
# zip_value = int("New York")
