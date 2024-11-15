# #Write a program to take the 2 user inputs
# #then sum the number
# #mul -> *
# #div -> /
#
# #Logic Building
# # Step 1
# # I/P - > num 1, num 2 -> int (DAA-Dont Assume Anything- ask from the user)
# #O/P -> sum - int, sub, -> int, but div -> float in nature
# num1 = input("Enter the num 1")#as this is string so output would be error
# num2 = input("Enter the num 2")#as this is string so output would be error
# print(type(num1))
#print(type(num2))

# #so what we have to do-->convert str to int like below:
num1 = int(input("Enter the num 1->"))#or-->num1 = int(num1)
num2 = int(input("Enter the num 2->"))#or-->num2 = int(num2)
#
# # Step 2
# #sum +, sub -, mul *, div /
#
# # Step 3
sum = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
print ("Sum is -->", sum)
print ("Sub is -->", sub)
print ("Mul is -->", mul)
print ("Div is -->", div)
#
#
# #num1 155
#num2 5