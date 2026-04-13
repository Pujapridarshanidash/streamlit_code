def add (x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
     return "Error!Division by zero."
    return x/y
print("Simple calculator:")
print("Choose an operation:")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
while True:
    choice=input("\nEnter choice (1/2/3/4 or 'quit' to exit):")
    if choice=='quit':
        print("Goodbye!")
    if choice in ['1','2','3','4']:
        num1=float(input("enter first number:"))
        num2=float(input("Enter second number:"))
        if choice=='1':
          print("Result:",add(num1,num2))
    elif choice=='2':
        print("result:",substract(num1,num2))
    elif choice=='3':
        print("result:",multiply(num1,num2))
    elif choice=='4':
        print("result:",divide(num1,num2))
    else:
        print("Invalid input ! please try again.")