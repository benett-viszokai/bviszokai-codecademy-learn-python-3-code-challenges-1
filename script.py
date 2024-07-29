# I. Control Flow (Basic)

# 1. Not Sum To Ten

# You are given two numbers stored in num1 and num2. If the sum of num1 and num2 is NOT equal to 10, then store True into a variable called not_ten, otherwise store False in not_ten.

num1 = 6
num2 = 3

# Write your if statement here
if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

# Uncomment the below lines to show the result
print("Does the sum of the numbers equal 10? " + str(not_ten))

# 2. Over Budget

# You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget!
# First, store the total of all expenses into a variable called total.
# Next, check if the total is greater than the budget. If it is, store True into a variable called over_budget, otherwise store False in over_budget.

# Monthly budget
budget = 2000

# Monthly expenses
food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

# Calculate the total amount of expenses
total = food_bill + electricity_bill + internet_bill + rent

# Check if the total is greater than the budget and store the result in over_budget
if total > budget:
  over_budget = True
else:
  over_budget = False

# Uncomment the below lines to see the results

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))

# 3. Large Power

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False

# Write your large_power function here:
def large_power(base, exponent):
  if (base ** exponent) > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# 4. Twice as Large

# Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# 5. Divisible By Ten

# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

########################################################################################################################################################

# II. Control Flow (Advanced)

# 1. In Range

# Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Write your in_range function here:
def in_range(num, lower, upper):
  if (num >= lower) and (num <= upper):
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# 2. Same Name

# Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# 3. Always False

# Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

# Write your always_false function here:
def always_false(num):
  if (num >= 0) or (num <= 0):
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# 4. Movie Review

# Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:
def movie_review(rating):
  if rating >= 9:
    return "Outstanding!"
  elif rating >= 5:
    return "This was fun."
  else:
    return "Avoid at all costs!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

# 5. Max Number

# Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

# Write your max_num function here:
def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num1 and num3 > num2:
    return num3
  else:
    return "It's a tie!"
  
# Uncomment these function calls to test your max_num function:
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"

########################################################################################################################################################

# III. Lists (Basic)

# 1. Append Size

# Create a function called append_size that has one parameter named my_list.
# The function should append the size of my_list (inclusive) to the end of my_list. The function should then return this new list.
# For example, if my_list was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of my_list was originally 3.

#Write your function here
def append_size(my_list):
 my_list.append(len(my_list))
 return my_list

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 2. Append Sum

# Write a function named append_sum that has one parameter — a list named named my_list.
# The function should add the last two elements of my_list together and append the result to my_list. It should do this process three times and then return my_list.
# For example, if my_list started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

#Write your function here
def append_sum(my_list):
  i = 0
  while i < 3:
    my_list.append(my_list[-1] + my_list[-2])
    i += 1
  return my_list
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# 3. Larger List

# Write a function named larger_list that has two parameters named my_list1 and my_list2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of my_list1.

#Write your function here
def larger_list(my_list1, my_list2):
  if len(my_list2) > len(my_list1):
    return my_list2[-1]
  else:
    return my_list1[-1]
#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4. More Than N

# Create a function named more_than_n that has three parameters named my_list, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

#Write your function here
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 5. Combine Sort

# Write a function named combine_sort that has two parameters named my_list1 and my_list2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

#Write your function here
def combine_sort(my_list1, my_list2):
  combined_list = my_list1 + my_list2
  combined_list.sort()
  return combined_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
