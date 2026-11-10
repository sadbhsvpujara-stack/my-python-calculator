print("---Crypto Wallet Manager---")
wallet = {"BTC": 0.5, "ETH": 2.0, "SOL": 10.0}

def show_balances(wallet):
    for key,value in wallet.items():
        print(f"{key} : {value}")

def add_crypto(wallet):
    coin_name = input("Enter your coin name:")
    amount_to_add = float(input("Enter the amount to add:"))
    if coin_name in wallet:
        wallet[coin_name]+= amount_to_add
        print(f"Updated data:\{coin_name}:{amount_to_add}")
    else:
        wallet[coin_name] = amount_to_add
        print(f"Updated data:\n{coin_name}:{amount_to_add}")

    print(wallet, end="\n")
print(f"1. View Balance\n 2. Add crypto\n 3. Exit\n")

while True:
    user_input = int(input("Choose a number:"))
    if user_input == 1:
        show_balances(wallet)
    elif user_input == 2:
        add_crypto(wallet)
    elif user_input == 3:
        break
    else:
        print(f"Please input a valid input!")

    