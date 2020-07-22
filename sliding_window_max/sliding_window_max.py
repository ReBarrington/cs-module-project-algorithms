'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    output = []
    
    for i in range(len(arr)):
        # window = Slice list by k
        window = arr[i:i+k]

        # if window is cut short bc end of list, return output
        if len(window) != k:
            return output

        # return largest num in window to output
        output.append(max(window))


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
