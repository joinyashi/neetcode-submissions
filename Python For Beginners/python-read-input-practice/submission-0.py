def add_two_numbers() -> int:
    user = input()
    sums = user.split(",")
    a = 0
    for i in sums:
        a += int(i)
        
    return a


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
