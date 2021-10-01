def divide(a, b):
    try:
        return a / b
    except Exception as ex:
        return f"Error: {ex}"


print(divide(4, 0))
print(divide(4, 'asd'))
print(divide(0, 4))
