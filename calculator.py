print("Select operation.")

print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")

num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))

Operation = input("Select Operation (1/2/3/4):")
if Operation == '1':
    print(num1, "+", num2, "=", num1 + num2)

elif Operation == '2':
    print(num1, "-", num2, "=", num1 - num2)


elif Operation == '3':
    print(num1, "*", num2, "=", num1 * num2)

elif Operation == '4':
    print(num1, "/", num2, "=", num1 / num2)

else:    print("Invalid Input")