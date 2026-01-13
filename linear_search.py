# linear search is the basic searching technique which is used basically, but it is not the efficient, but it is mandatory to know about this, and it may be used in brute force solutions in some problems. And also it takes the time complexity of O(n)

def linear_search(nums, key): # function initialization
    for i in range(len(nums)): # loop to iterate through the list of values
        if nums[i] == key: # condition to check whether the key value in the list or not
            return i # if key value is found in the list it returns the index value
    return -1 # if key value is not found in the list it returns -1

numbers = list(map(int, input("Enter the list of values: ").split())) # seeking input from the user and make it as a list
key_value = int(input("Enter the key value to find: ")) # seeking the input from user, value to find in the list
result = linear_search(numbers,key_value) # calling the linear_search function
print(f"✅ Value found at index position -> {result}" if result >= 0 else "❎ Value not found!") # validating the output from the function that itis found or not

