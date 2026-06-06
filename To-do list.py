tasks = []

while True:
    print("\n1. Task add karo")
    print("2. Saare tasks dekho")
    print("3. Task delete karo")
    print("4. Exit")
    
    choice = input("Option chuno 1-4: ")
    
    if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("Task add ho gaya ✅")
    
    elif choice == "2":
        if len(tasks) == 0:
            print("Koi task nahi hai")
        else:
            print("\nTumhare tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")
    
    elif choice == "3":
        num = int(input("Kaunsa number delete karu: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Delete ho gaya")
        else:
            print("Galat number")
    
    elif choice == "4":
        print("Bye!")
        break
