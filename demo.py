print("Hello")
print(" This is a Bug Fix branch ")
print("this is to check tag a branch")
print("This is stash changes .!!!!!")
# change the value for a different result

factorial = 7

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
