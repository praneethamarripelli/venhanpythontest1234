def is_Prime(number):
    if number > 1:
        for p in range(2,number):
            if number % p == 0:
                return False 
    return True 
print(is_Prime(6))