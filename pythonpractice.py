#Write a program to remove characters from a string starting from zero up to n and return a new string.
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

#Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
def first_last_same(numberList):
    print("Given list:", numberList)
    
    first_num = numberList[0]
    last_num = numberList[-1]
    
    if first_num == last_num:
        return True
    else:
        return False

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

# Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

# Exercise Functions
# Highest Even: Write a function to find the highest even number from the list.
def highest_even(li):
    evens = []
    for item in li:
        if not item % 2 and item not in evens:
            evens.append(item)
    return max(evens)

print(highest_even([10, 2, 3, 4, 8, 11]))

#Exercise 12: Calculate income tax for the given income by adhering to the rules below
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0
    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100
    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

#Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
res = list()

odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

#Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

