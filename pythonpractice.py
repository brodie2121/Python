#Write a program to remove characters from a string starting from zero up to n and return a new string.
def first_last_same(numberList):
  print("Given list:", numberList)

  first_num = numberList[0]
  last_num = numberList[-1]

  return first_num == last_num

numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))