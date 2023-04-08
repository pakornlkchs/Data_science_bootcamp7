def order_pizza():
    orders = []
    pizza_menu = ["Hawaiian", "Meat deluxe", "Pepporoni"]
    pasta_menu = ["Spaghetti Carbonara", "Chilli bacon pasta", "Mushroom cream spaghetti"]
    soup_menu = ["Corn soup", "Pumpkin soup", "Mushroom soup"]
    drinks_menu = ["Cola", "Water", "Orange juice"]

    print("Hi, welcome to Italia Pizzaria.")
    menu = input("""What would you like today?
    (please select by number) 
    [1] Pizza
    [2] Pasta
    [3] Soup
    [4] Drinks
    [5] No, Thanks
    """)
    
    while int(menu) != 5:
        if int(menu) == 1:
            pizza_toppings = input("Okay! what pizza topping would you like?\n[1] Hawaiian\n[2] Meat deluxe\n[3] Pepporoni\n ")
            pizza_size = input("What size do you want (S/M/L)? ")
            pizza_order = pizza_menu[int(pizza_toppings) - 1] + " pizza: " + pizza_size + " size"
            orders.append(pizza_order)
        elif int(menu) == 2:
            pasta = input(f"Nice! Which kind of pasta would you like?\n[1] Spaghetti Carbonara\n[2] Chilli bacon pasta\n[3] Mushroom cream spaghetti\n")
            orders.append(pasta_menu[int(pasta) - 1])
        elif int(menu) == 3:
            soup = input("What kind of soup would you like?\n[1] Corn soup\n[2] Pumpkin soup\n[3] Mushroom soup\n")
            orders.append(soup_menu[int(soup) - 1])
        elif int(menu) == 4:
            drinks = input("We have [1] Cola, [2] Water, and [3] Orange juice. What would you like? ")
            orders.append(drinks_menu[int(drinks) -1])
        else:
            print("please choose number between 1 - 5")
        menu = input("""anything else? (please select by number)
        [1] Pizza
        [2] Pasta
        [3] Soup
        [4] Drinks
        [5] No, Thanks 
        """)

    if (len(orders) == 0 and int(menu) == 5):
        print("Maybe we can serve you next time :)")

    else:
        print("Okay! Let me repeat your order.")
        count = 0
        for order in orders:
            count += 1
            print(str(count) + ". " +  order)

        print("Thank you for time, your food will be ready in 5 minutes")
        
        
order_pizza()
