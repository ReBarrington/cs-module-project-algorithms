'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n, count=0):

    if n <= 0:
        count += 1
        return count

    # 3 at a time
    if n > 2:
        count = eating_cookies(n-3, count)
    
    # 2 at a time
    if n > 1:
        count = eating_cookies(n-2, count)

    # 1 at a time
    if n > 0:
        count = eating_cookies(n-1, count)

    return count

# def eating_cookies(n, cache=None):
#     # base cases
#     if n < 0:
#         return 0
#     elif n == 0:
#         return 1
#     # check if answer already in cache
#     elif cache is not None and cache[n] > 0:
#         # return previously computed answer and dont recurse
#         return cache[n]
#     else:
#         # initialize an empty list for a cache
#         if cache is None:
#             cache = [0 for i in range(n+1)]
#         cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#     return cache[n]

  

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
