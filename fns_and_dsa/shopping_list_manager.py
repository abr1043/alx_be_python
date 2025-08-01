        shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"Item '{item}' not found in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("Current shopping list:")
                for idx, itm in enumerate(shopping_list, start=1):
                    print(f"{idx}. {itm}")
            else:
                print("Shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

