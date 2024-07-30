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

########################################################################################################################################################

# IV. Lists (Advanced)

# 1. Every Three Numbers

# Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

#Write your function here
def every_three_nums(start):
  if start > 100:
    return []
  else:
    return list(range(start, 101, 3))

#Uncomment the line below when your function is done
print(every_three_nums(2))

# 2. Remove Middle

# Create a function named remove_middle which has three parameters named my_list, start, and end.
# The function should return a list where all elements in my_list with an index between start and end (inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

#Write your function here
def remove_middle(my_list, start, end):
  first_half = my_list[0:start]
  second_half = my_list[end + 1:]
  removed = first_half + second_half
  return removed

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 3. More Frequent Item

# Create a function named more_frequent_item that has three parameters named my_list, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in my_list.
# If the two items appear the same number of times, return item1.

#Write your function here
def more_frequent_item(my_list, item1, item2):
  if my_list.count(item2) > my_list.count(item1):
    return item2
  else:
    return item1
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2], 2, 3))

# 4. Double Index

# Create a function named double_index that has two parameters: a list named my_list and a single number named index.
# The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.
# If index is not a valid index, the function should return the original list.

#Write your function here
def double_index(my_list, index):
  if index > len(my_list) - 1:
    return my_list
  else:
    changed_index = my_list[index] * 2
    my_list[index] = changed_index
    return my_list

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 3))

# 5. Middle Item 

# Create a function called middle_element that has one parameter named my_list.
# If there are an odd number of elements in my_list, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

#Write your function here
def middle_element(my_list):
  if len(my_list) % 2 == 0:
    middle1 = my_list[round(len(my_list) / 2 - 1) ]
    middle2 = my_list[round(len(my_list) / 2)]
    return (middle1 + middle2) / 2
  else:
    return my_list[round(len(my_list) / 2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

########################################################################################################################################################

# V. Loops (Basic)

# 1. Divisible By Ten

# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

#Write your function here
def divisible_by_ten(nums):
  i = 0
  for num in nums:
    if num % 10 == 0:
      i += 1
  return i

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings

# Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

#Write your function here
def add_greetings(names):
  greetings = []
  for name in names:
    greetings.append("Hello, " + name)
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers

# Write a function called delete_starting_evens() that has a parameter named my_list.
# The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.
# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!

def delete_starting_evens(my_list):
  while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list

# 4. Odd Indices

# Create a function named odd_indices() that has one parameter named my_list.
# The function should create a new empty list and add every element from my_list that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

#Write your function here
def odd_indices(my_list):
  new_list = []
  i = 0
  while i < len(my_list):
    if i % 2 != 0:
      new_list.append(my_list[i])
    i += 1
  return new_list

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents

# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

#Write your function here
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base ** power)
  return new_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

########################################################################################################################################################

# VI. Loops (Advanced)

# 1. Larger Sum

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0

  for num in lst1:
    sum1 += num
  for num in lst2:
    sum2 += num

  if sum2 > sum1:
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

# 2. Over 9000

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Write your function here
def over_nine_thousand(lst):
  sum = 0
  i = 0

  while i < len(lst):
    if sum < 9000:
      sum += lst[i]
      i += 1
    else:
      return sum
  return sum
    
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num

# Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

#Write your function here
def max_num(nums):
  nums.sort()
  return nums[-1]

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]

#Write your function here
def same_values(lst1, lst2):
  new_list = []
  i = 0

  while i < len(lst1):
    if lst1[i] == lst2[i]:
      new_list.append(i)
    i += 1
  return new_list


#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# 5. Reversed List

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

#Write your function here
def reversed_list(lst1, lst2):
  lst2.sort() 
  if lst1 == lst2:
    return True
  else:
    return False

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

########################################################################################################################################################

# VII. Functions (Basic)

# 1. Tenth Power

# Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# 2. Square Root

# Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

# Write your square_root function here:
def square_root(num):
  return num ** 0.5

# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 3. Win Percentage

# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
  return (wins + losses) / 100 * wins * 100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

# 4. Average

# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.

# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 5. Remainder

# Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.
# Write your remainder function here:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
  
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

########################################################################################################################################################

# VIII. Functions (Advanced)

# 1. First Three Multiples

# Write a function named first_three_multiples() that has one parameter named num.
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.

# Write your first_three_multiples function here
def first_three_multiples(num):
  i = 1
  while i < 4:
    print(num * i)
    i += 1
  return num * 3

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 2. Tip

# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.

# Write your tip function here:
def tip(total, percentage):
  return total * (percentage * 0.01)

# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0


# 3. Bond, James Bond

# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.

# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ', ' + first_name + ' ' + last_name
# Uncomment these function calls to test your introduction function:
print(introduction("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

# 4. Dog Years
# Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string:
"{name}, you are {age} years old in dog years"

# Write your dog_years function here:
def dog_years(name, age):
  return name + ", you are " + str(age * 7) + " years old in dog years"
# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

# 5. All Operations

# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  first = a + b
  print(first)
  second = c - d
  print(second)
  third = first * second
  print(third)
  return third % a

# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
