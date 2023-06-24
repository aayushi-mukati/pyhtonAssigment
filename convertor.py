# This function adds two numbers
def gram(kilograms):
    return kilograms * 1000

# This function subtracts two numbers
def kilogram(grams):
    return grams / 1000

# This function multiplies two numbers
def celcius(fahr):
    return (fahr-32) / 1.8

# This function divides two numbers
def fahrenheit(celcius):
    return (celcius * 1.8) + 32

def second(hours):
    return hours * 3600

def hour(seconds):
    return seconds //3600


print("Select operation.")
print("1.Gram to Kilogram")
print("2.kilogram to gram")
print("3.celcius to fahrenhiet")
print("4.fahrenhiet to celcius")
print("5.hour to second")
print("6.second to hour")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4','5','6'):
        try:
            num1 = float(input("Enter number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(kilogram(num1))

        elif choice == '2':
            print(gram(num1))

        elif choice == '3':
            print(fahrenheit(num1))

        elif choice == '4':
            print(celcius(num1))
            
        elif choice == '5':
            print(second(num1))
            
        elif choice == '6':
            print(hour(num1))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")