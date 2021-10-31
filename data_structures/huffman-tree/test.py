# def palindrome(x):
#     ret_val = " . -----   TRUE ------"
#     s = str(x)
#     for i in range(int(len(s))):
#         if s[i] != s[(i+1)*-1]:
#             ret_val = "----- False ......"
    
#     return ret_val

# x= palindrome("121")
# print(x)

def sum_two( nums, target):
    check = {}
    for i in range(len(nums)):
        b = target - nums[i]
        if b in check:
            return [check[b], i]
        else:
            check[nums[i]] = i
    
    pass

a = sum_two([2,5,5,7,10], 12)
print(a)
    


                    