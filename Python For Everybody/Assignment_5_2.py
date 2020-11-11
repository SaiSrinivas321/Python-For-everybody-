largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == "done" : break

    try:
        num1=int(num)

    except:
        print("Invalid input")



    if smallest is None:
        smallest=num1
    elif smallest>num1:
        smallest=num1

    if largest is None:
        largest=num1
    elif largest<num1:
        largest=num1


print("Maximum is", largest)
print("Minimum is", smallest)
