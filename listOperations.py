# This function adds two numbers
def merge():
    # creating an empty list
    lst1 = []
    lst2= []
    # number of elements as input
    n1 = int(input("Enter size of first list : "))
    print("Enter elements :")
    # iterating till the range
    for i in range(0, n1):
        ele = int(input())
        # adding the element
        lst1.append(ele)
        
    n2 = int(input("Enter size of second list : "))
    print("Enter elements :")
    # iterating till the range
    for i in range(0, n2):
        ele = int(input())
        # adding the element
        lst2.append(ele)  
        
    size_1 = len(lst1)
    size_2 = len(lst2)
    res = []
    i, j = 0, 0
    while i < size_1 and j < size_2:
        if lst1[i] < lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res = res + lst1[i:] + lst2[j:]    
    return "output = "+str(res)

# This function subtracts two numbers
def interchange():
    lst = []
    n1 = int(input("Enter size of list : "))
    print("Enter elements :")
    # iterating till the range
    for i in range(0, n1):
        ele = int(input())
        # adding the element
        lst.append(ele)
    size = len(lst)
    temp = lst[0]
    lst[0] = lst[size - 1]
    lst[size - 1] = temp
    return "output = "+str(lst)

# This function multiplies two numbers
def even():
    lst =[]
    result =[]
    n1 = int(input("Enter size of list : "))
    print("Enter elements :")
    # iterating till the range
    for i in range(0, n1):
        ele = int(input())
        # adding the element
        lst.append(ele)
        
    for num in lst:
        # checking condition
        if num % 2 == 0:
           result.append(num) 
       
    return "output"+str(result)

# This function divides two numbers
def ascending():
    lst =[]
    result =[]
    n1 = int(input("Enter size of list : "))
    print("Enter elements :")
    # iterating till the range
    for i in range(0, n1):
        ele = int(input())
        # adding the element
        lst.append(ele)
        
    if sorted(lst) == lst:
       return True
    else:
       return False

print("Select list operation.")
print("1.merge")
print("2.interchange first and last element of a list")
print("3.find even number from a list")
print("4.check if list is ascending order")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print(merge())

        elif choice == '2':
            print(interchange())

        elif choice == '3':
            print(even())

        elif choice == '4':
            print(ascending())
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")