'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    repeated = []
    for i_in_arr in range(len(arr)):
        i_of_unchecked = i_in_arr + 1
        for i_in_arr_compare in range (i_of_unchecked, len(arr)):
            if arr[i_in_arr] == arr[i_in_arr_compare]:
                repeated.append(arr[i_in_arr])
        if arr[i_in_arr] not in repeated:
            return arr[i_in_arr]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")