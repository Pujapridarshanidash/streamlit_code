l={-45,34,-44,56,-68}
print("positive elements are")
for i in l:
    if i>=0:
        print(i)
        print("negative elements are")
        for i in l:
            if i<0:
                print(i)