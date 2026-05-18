#Print all the possible combinations when we press 3 keys on the phone keypad.
keypad=["", "", "abc", "def", "ghi", "jkl","mno", "pqrs", "tuv", "wxyz"]
def print_keypad(combinations,curr,output,n):
    if curr==n:
        print(" ".join(output))
        return
    digit=combinations[curr]
    if digit==0 or digit==1:
        print_keypad(combinations,curr+1,output,n)
        return
    for ch in keypad[digit]:
        output.append(ch)
        print_keypad(combinations,curr+1,output,n)
        output.pop()
combinations=[4,3,4]
n=len(combinations)
print_keypad(combinations,0,[],n)
