
  #Addition for input numbers 
numbers = [20,3,5]  # Take input as a string
sum1 = 0  # Initialize the sum

for i in numbers: 
    sum1 = sum1 + i # Convert each character to an integer and add to sum 
    print("The current sum is:", sum1)

print("The total addition is:", sum1)  # Print the final sum




  #Addition for input numbers 
no = input("Enter the number: ")  # Take input as a string
sum2 = 0  # Initialize the sum

for i in no:
    sum2 = sum2 + int(i)  # Convert each character to an integer and add to sum
    print("The current sum is:", sum2)

print("The total addition is:", sum2)  # Print the final sum

#difference of 2 numbers 
no3 = [20,2,1]
difference =  no3[0]

for i in no3[1:]:
    difference = difference - i
    print("The current difference is", difference)

print("The final difference is", difference)
 
 # multiplication 
 # Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Multiplying the numbers
product = num1 * num2

# Displaying the result
print(f"The product of {num1} and {num2} is {product}")


     # multiplication with predefined numbers 
# Predefined numbers
num1 = 7
num2 = 8


# Multiplying the numbers
product = num1 * num2
print("the product ", type(product))
print("the product " , product) 


# Displaying the result
print(f"The product of {num1} and {num2} is {product}")



# Define two lists
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Check if both lists are of the same length
if len(list1) == len(list2):
    # Multiply corresponding elements
    result = [list1[i] * list2[i] for i in range(len(list1))]
    print("The result of multiplying the two lists is:", result)
else:
    print("The two lists must have the same length!")



list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Multiply corresponding elements using zip
result = [x * y for x, y in zip(list1, list2)]
print("The result of multiplying the two lists is:", result)



#zip(list1, list2):

#The zip() function combines two lists (list1 and list2) into pairs of corresponding elements.

#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#zip(list1, list2)  # Produces: [(1, 4), (2, 5), (3, 6)]

#for x, y in zip(list1, list2):

# This iterates over the pairs produced by zip():
# On the first iteration: x = 1, y = 4.
# On the second iteration: x = 2, y = 5.
# On the third iteration: x = 3, y = 6.






















