items = [
    {
        "item": "Fruit Juice",
        "price": 8
    },
    {
        "item": "Biscuits",
        "price": 4
    },
    {
        "item": "Soda Drinks",
        "price": 6
    },
    {
        "item": "Ice Creams",
        "price": 12
    }
]

def shopping_automation():
    while True:
        print("""
        Which item do you want?
            1. Fruit Juice ------- $8
            2. Biscuits -------- $4
            3. Soda Drinks -------- $6
            4. Ice Creams -------- $12
            0. To exit
              """)
        user_choice = int(input("Choose the item: "))
        if user_choice == 0:
            print("See you later!")
            break
        elif user_choice != 0 and user_choice <= 4 and user_choice >= 1:
            amount = int(input("How many of them u want?: "))
            user_choice_price = items[user_choice - 1]["price"]
            user_choice_item = items[user_choice - 1]["item"]
            total = amount * user_choice_price
            print(f"Hello sir/madam u ordered {amount} of {user_choice_item}/s. Which totally costs ${total}!")
        else:
            if user_choice > 4 or user_choice < 0:
                print("Sorry invalid option try again!")

shopping_automation()
