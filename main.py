# Conditions

# if condition
marks  = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks < 35:
    print("W")
elif marks < 55:
    print("S")
elif marks < 65:
    print("C")
elif marks < 75:
    print("B")
else:
    print("A")



