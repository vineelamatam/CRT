'''
Time Complexity:
Definition: Time Complexity can be measure based upon the input
Ex:
n = 10
print(n)

O(1) --> Constant Time
o(n) -->single loop
o(n^2) --> Two loop
o(log n) --> Binary Search
o(n log n) --> linearithmic
o(2^n) --> Recursions
#Brute Force --> step by step execute,high complexity,neglects the efficiency
#Optimal Solution --> needs thinking,low complexity
print("Time Complexity")
arr=[1,2,3,4,5]
for i in arr:
    print(i)
    def linear_search(arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    print(linear_search([10,20,30,40,58,46],10))
    print(linear_search([10,20,30,40,58,46],46))
    print(linear_search([10,20,30,40,58,46],30))

'''

    
    