#IF ELIF ELSE

#recall that if else is used by python to run a code if the "if condition" is True
# or it runs "else" if the "if condition" is False


#elif means Else If
#elif is simply used to add more options/conditions to your code
#elif MUST be after your IF and before your ELSE
#You can have as many as possible elif in your code


name = input("Please enter your name: ")

maths = int(input('Enter Maths score: '))

# 90 above A+
# 80-89 A
# 70-79 B
# 60-69 C
# 50-59 D
#49 below is F

if (maths > 90): #condition, remember to end with a colon
    print("You got an A+")
    print("You passed the test") 
    print("Congratulations") 

elif (maths >=80) and (maths <=89):
    print('You got an A')
    print("You passed the test") 
    print("Congratulations") 

else: #condition, remember to end with a colon
    print('You got an F')
    print("You failed the test") 
    print("Sorry try again later") 

