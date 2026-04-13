
def palindrome(st):
    rev = "" 
    for i in range(len(st)-1, -1, -1):
        rev += st[i]
    if rev == st:
        print(f"{st}Palindrome")
    else:
        print(f"{st}Not a palindrome")