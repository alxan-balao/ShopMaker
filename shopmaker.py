def identify_category(cid):
    categories = {
        "cid": "AthenaCharacter",
        "bid": "AthenaBackpack",
        "pickaxe_id": "AthenaPickaxe",
        "glider_id": "AthenaGlider",
        "eid": "AthenaDance"
    }
    type = cid.split(":")[0].split("_")[0].lower()
    return categories.get(type, None), cid

def add_items(category_prefix, num_items):
    items = {}
    for i in range(1, num_items + 1):
        category = f"{category_prefix}{i}"
        print(f"\nAdd items for {category}:")
        while True:
            try:
                cid = input("Enter the ID of the item: ")
                if not cid:
                    raise ValueError("ID cannot be empty.")
                price = int(input("Enter the price of the item: "))
                if price <= 0:
                    raise ValueError("Price must be a positive integer.")
                type, full_type = identify_category(cid)
                if type:
                    items[category] = {}
                    items[category]["itemGrants"] = [f"{type}:{full_type}"]
                    items[category]["price"] = price
                    break
                else:
                    print("Unknown item type. Please enter a valid ID.")
            except ValueError as e:
                print(f"Error: {e}")
    return items

def main():
    while True:
        print('''
░██████╗██╗░░██╗░█████╗░██████╗░███╗░░░███╗░█████╗░██╗░░██╗███████╗██████╗░
██╔════╝██║░░██║██╔══██╗██╔══██╗████╗░████║██╔══██╗██║░██╔╝██╔════╝██╔══██╗
╚█████╗░███████║██║░░██║██████╔╝██╔████╔██║███████║█████═╝░█████╗░░██████╔╝
░╚═══██╗██╔══██║██║░░██║██╔═══╝░██║╚██╔╝██║██╔══██║██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝██║░░██║╚█████╔╝██║░░░░░██║░╚═╝░██║██║░░██║██║░╚██╗███████╗██║░░██║
╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
''')
        print("Made by balaorapido")
        choice = input("Type 'start' to configure the shop or 'exit' to quit: ").lower()
        if choice == 'start':
            shop = {}
            num_daily = int(input("Enter the number of daily items: "))
            num_featured = int(input("Enter the number of featured items: "))

            shop.update(add_items("daily", num_daily))
            shop.update(add_items("featured", num_featured))

            print("\nThe BR Item Shop Config is as follows:")
            print("{")
            print('    "//": "BR Item Shop Config",')
            for i, (category, data) in enumerate(shop.items()):
                print(f'    "{category}": {{')
                print(f'        "itemGrants": ["{data["itemGrants"][0]}"],')
                print(f'        "price": {data["price"]}')
                if i < len(shop) - 1:
                    print("    },")
                else:
                    print("    }")
            print("}")
            print()
            while True:
                edit_choice = input("Type 'edit' to modify items or 'exit' to quit: ").lower()
                if edit_choice == 'edit':
                    item_to_edit = input("Enter the category of the item you want to edit (e.g., daily1): ")
                    if item_to_edit in shop:
                        new_cid = input("Enter the new ID for the item: ")
                        new_price = int(input("Enter the new price for the item: "))
                        type, full_type = identify_category(new_cid)
                        if type:
                            shop[item_to_edit]["itemGrants"] = [f"{type}:{full_type}"]
                            shop[item_to_edit]["price"] = new_price
                            print("Item updated successfully.")
                        else:
                            print("Unknown item type. Item not updated.")
                    else:
                        print("Invalid item category. Please try again.")
                elif edit_choice == 'exit':
                    break
                else:
                    print("Invalid choice. Please type 'edit' to modify items or 'exit' to quit.")
            break
        elif choice == 'exit':
            break
        else:
            print("Invalid choice. Please type 'start' to configure the shop or 'exit' to quit.")

if __name__ == "__main__":
    main()
