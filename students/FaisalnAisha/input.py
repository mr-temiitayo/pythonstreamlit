#INPUT STATEMENT
#Input statement is used to ask the user a question and save their input/response/answer in a variable

# name = input('Enter your name: ')

# gender = input('Enter your gender: ')

# age = input('Enter your age: ')

# print("my name is",name+", I am a",gender,'and I am',age,'years old')


"""
Classwork 1:
A fuel station sells a litre of fuel for 20$. 
Create a program in Python to ask how many litres people want to get and then tell them the total price
"""


litre = 20 #integer
print("A litre of fuel cost $20")
quantity = input("How many litres do you want: ") #string
total = litre*int(quantity)
print("The total cost for",litre,'litres is',total,'dollars')

#int to str
#str to int
# float to str
# str to float
# bool to str
# str to bool