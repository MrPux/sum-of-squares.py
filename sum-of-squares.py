# sum_of_squares([1, 2, 3, 4])  # Should return 30 (1^2 + 2^2 + 3^2 + 4^2)
def sum_of_squares(list):
    return sum([i ** 2 for i in list])
print(sum_of_squares([1, 2, 3, 4])) # Prints 30