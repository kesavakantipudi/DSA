# Binary Search in an efficient searching technique, But it not like a linear search it requires the sorted array or list to perform the search operation, and it reduces the time complexity as compared to the linear search, time complexity for this searching algorithm is O(log n)
def binary_search(nums, key):   # function initialization
    low, high = 0, len(nums)-1  # initializing low & high variables to traverse through the list
    while low < high:   # initializing a loop to traverse through the list, and it stops when low equals or more than high
        mid = (high + low) // 2     # finding mid value
        if nums[mid] == key:    # comparing whether the mid-value is key or not
            return mid      # return the index if the value found
        if key > nums[mid]:     # if the key value is greater that the mid-value
            low = mid+1         # then low value is updated
        else:                   # if the key value is less than the mid-value
            high = mid-1        # then high value is updated
    return -1   # if key is not found then it returns -1

numbers = list(map(int, input("Enter the list of values: ").split()))   # seeking input from user for a list of values
key_value = int(input("Enter the key value to find: "))     # seeking input from user, value to find
result = binary_search(numbers, key_value)      # calling the binary_search function by sending the arguments
print(f"✅ Value found at index position -> {result}" if result >= 0 else "❎ Value not found!") # validating the output from the function and displaying th output


