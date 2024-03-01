while True:
    user_value = int(input("Enter a value that is a multiple of 10 between 100 and 1000: "))
    if 100 <= user_value <= 1000 and user_value % 10 == 0:
        break
    else:
        print("Invalid input. Please ensure your value is a multiple of 10 between 100 and 1000.")

values = []
for i in range(1, 11):
    if i % 3 == 0:
        value = i * 0.3 * user_value
    else:
        value = i * 0.1 * user_value
    values.append(value)

choice = input("Do you want the sum of values at odd or even positions? (Enter 'odd' or 'even'): ").lower()
while choice not in ['odd', 'even']:
    choice = input("Invalid choice. Please enter 'odd' or 'even': ").lower()

sum_result = 0
if choice == 'odd':
    sum_result = sum(values[i] for i in range(0, 10, 2))
else:
    sum_result = sum(values[i] for i in range(1, 10, 2))
  
print(f"The result of the sum is: {sum_result}")

