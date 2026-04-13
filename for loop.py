a=range(1,31,1)
for i in a:
    print(i)
#or
for i in range(31):
    print(i)
#in reverse order for loop
for i in range(16,-1,-1):
    print(i)
#lets print a table of 5
n=int(input("which table you want?"))
for i in range(n,(n*10)+1,n):
    print(i)