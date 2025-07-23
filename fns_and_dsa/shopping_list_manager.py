def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == '1':
            # Prompt for and add an item
            item = input('Enter the item to add: ') 
            shopping_list.append(item)
            print(f"'{item}' added to the shopping list.")
            pass
        elif choice == '2':
            remove_item = input("Item name to remove:")
            if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
            else:
                    print(f"{remove_item} is not in shopping list")
            # Prompt for and remove an item
            pass
        elif choice == '3':
            print(shopping_list)
            # Display the shopping list
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
