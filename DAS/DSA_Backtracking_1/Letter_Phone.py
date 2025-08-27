
# steps to proceed with this problem:
# step1: define a hashmap for all the numbers..
# step2: use the back_tacking approach to get all the possible combination for given numbers....
# step3: define a base condition
# step4: start with a loop which will check all the numbers in a respective number
# step5: append the current number in a temporary list and repeat.....
# step6: backtrack by removing the last element



def letter_phone(A:str, hashmap:dict, idx:int = 0, current_list=None, ans=None):
    if current_list is None:
        current_list = []
    if ans is None:
        ans = []

    # step3: base condition
    if idx == len(A):
        ans.append(''.join(current_list))
        return ans
    # step4: start with a loop which will check all the numbers in a respective number
    for item in hashmap[A[idx]]:
        # step5: append the current number in a temporary list and repeat.....
        current_list.append(item)
        letter_phone(A, hashmap, idx+1, current_list, ans)
        current_list.pop() # step6: backtrack by removing the last element
    return ans


hashmap = {'0': '0','1': '1' ,'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
A = "23"
A = "201"
print(letter_phone(A, hashmap))


