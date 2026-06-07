numbers = []
print("Number Analyzer shuru!")
print("Number likho. Stop karne ke liye 'done' likho\n")

# User se numbers lena
while True:
    num = input("Number enter karo: ")
    if num.lower() == 'done':
        break
    numbers.append(float(num))

# Analysis
if len(numbers) > 0:
    print("\n=== Results ===")
    print(f"Total numbers: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Sorted list: {sorted(numbers)}")
else:
    print("Koi number enter nahi kiya!")
