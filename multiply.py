def multiply(num1, num2):
    if num2 == 1:
        """
        """
        return num1

    return num1 + multiply(num1, num2-1)

print(multiply(-9, 4))