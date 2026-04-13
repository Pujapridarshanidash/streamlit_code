#count vowels
s=input("please enter your number:")
vowels="aeiouAEIOU"
count=sum(1 for ch in s if ch in vowels)
print("Number of vowels:",count)