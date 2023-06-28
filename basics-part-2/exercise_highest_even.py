def highest_even(a_list):
    evens_list = []
    for num in a_list:
        if num % 2 == 0:
            evens_list.append(num)
    return max(evens_list)


nums_list = [10, 2, 3, 4, 8, 11]
print(highest_even(nums_list)) 