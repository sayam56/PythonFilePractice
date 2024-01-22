# Define the list of categories
L1 = ['tea', 'bakery', 'soaps', 'rice', 'candies', 'lotions']

d1 = {}

# opening the file in read mode
with open("grocerylist.txt", "r") as file:
    while True:
        #reading the first line of file as category
        cat = file.readline().strip()
        
        if not cat:
            break #breaking out of the loop if there is no more category to read
        
        item = file.readline().strip()
        qty = file.readline().strip()
        
        #skipping the next newline character in the txt file
        file.readline()
        
        if cat in L1:
            # if cat is found then save into the dictionary
            d1[cat] = (item,int(qty))
        else:
            # if not found print message
            print("The category", str(cat), "is not available.")
            
#print(d1)

while True:
    #taking user input
    s = input("Please enter a category: ")

    try:
        # checking if s is in d1
        if d1[s]:
            print("Found Category: ", str(s))
            item, qty  = d1[s]
            print("Item:", str(item), ", Quantity:", str(qty))
            
            while True:
                # asking the user to enter a number
                n = input("How many items would you like to order? ")
                
                try:
                    # checking if n is an integer
                    n = int(n)
                    # print("n is integer")
                    if n == 0:
                        print("Order of zero quantity cannot be placed.")
                    elif n < 0:
                        # if n is negative int
                        print("Negative inputs are not accepted.")
                    else:
                        # if input is bigger than the existing quantity
                        if n > int(qty):
                            print("Sorry! Not enough quantity exists.")
                        else:
                            print("Congratulations – Your order is successfully placed.")
                            break
                except ValueError:
                    print("Input is not a valid integer.")
                    break
        break
    except KeyError:
        print("The entered category is not available. Please enter a different category.")
    