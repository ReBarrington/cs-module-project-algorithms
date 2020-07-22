'''
Input: an integer
Returns: an integer
'''

def eating_cookies(n):
    return recursive_eating_cookies(n)

def recursive_eating_cookies(n, count=0):

    if n <= 0:
        count += 1
        return count

    # 3 at a time
    if n > 2:
        count = recursive_eating_cookies(n-3, count)
    
    # 2 at a time
    if n > 1:
        count = recursive_eating_cookies(n-2, count)

    # 1 at a time
    if n > 0:
        count = recursive_eating_cookies(n-1, count)

    return count
  

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
