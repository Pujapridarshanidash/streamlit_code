l=[12,36,16,76,78,77,100]
largest=l[0]
index=0

for i in range(len(l)):
    if l[i] > largest:
        largest=l[i]
        index=i
    print(f"your largest number is {largest} at index{index}")