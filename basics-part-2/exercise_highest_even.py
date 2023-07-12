def highest_even(a_list):
    evens_list = []
    for num in a_list:
        if num % 2 == 0:
            evens_list.append(num)
    return max(evens_list)


nums_list = [10, 2, 3, 4, 8, 11]
print(highest_even(nums_list))


# another method using looping instead of the built in max / min functions
def highest_even2(a_list):
    evens_list = []
    for num in a_list:
        if num % 2 == 0:
            evens_list.append(num)
    
    highest_even = evens_list[0]
    lowest_even = evens_list[0]
    for even_num in evens_list:
        if even_num > highest_even:
            highest_even = even_num
        elif even_num < lowest_even:
            lowest_even = even_num

    print(f"The highest even is {highest_even}")
    print(f"The lowest even is {lowest_even}")
    return (highest_even, lowest_even)

print(highest_even2(nums_list))