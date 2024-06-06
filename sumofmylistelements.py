def sum_of_squares(list):
    return sum(x**2 for x in list)

numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum_of_squares(numbers)
print("Sum of Squares:",sum_of_squares)
