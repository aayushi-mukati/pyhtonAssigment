# This function adds two numbers
def sum():
    test_tup = (1,2,3,4,5)
    # Converting into list
    test = list(test_tup)
    # Initializing count
    count = 0
    # for loop
    for i in test:
        count = count+ i
        
    return str(count)
    
    
# This function multiplies two numbers
def sort():
    tup = [("Amana", 28), ("Zenat", 30), ("Abhishek", 29),
        ("Nikhil", 21), ("B", "C")]
    n = len(tup)
    for i in range(n):
        for j in range(n-i-1):
            if tup[j][0] > tup[j + 1][0]:
                tup[j], tup[j + 1] = tup[j + 1], tup[j]
                 
    return tup        

# This function divides two numbers
def find():
    num = int(input("Enter number to find : "))
    t = (25, 17, 55, 63, 40)
    for i in range(len(t)):
        if t[i]== num:
           return "number found"
    return "number not found"
    
    
print("Select tuple operation.")
print("1.sum ")
print("2.sort alphabetically")
print("3.find number present or not in tuple")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3'):
        if choice == '1':
            print(sum())

        elif choice == '2':
            print(sort())

        elif choice == '3':
            print(find())
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")