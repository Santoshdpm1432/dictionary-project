santosh_dictionary = {}  

while True:
    print("\nDictionary Management System")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        word = input("Enter the word: ").strip().lower()
        if word in santosh_dictionary:
            print("This word already exists in the dictionary.")
        else:
            meaning = input("Enter its meaning: ").strip()
            santosh_dictionary[word] = meaning
            print(f"Word '{word}' added successfully!")

    elif choice == "2":
        word = input("Enter the word to search: ").strip().lower()
        if word in santosh_dictionary:
            print(f"Meaning of '{word}': {santosh_dictionary[word]}")
        else:
            print("Word not found in the dictionary.")

    elif choice == "3":
        if santosh_dictionary:
            print(f"here is the total words and meanings: {santosh_dictionary} ")
        else:
            print("The dictionary is empty.")

    elif choice == "4":
         word = input("Enter the word to update: ").strip().lower()
         if word in santosh_dictionary:
            new_meaning = input("Enter the new meaning: ").strip()
            santosh_dictionary[word] = new_meaning
            print(f"Meaning of '{word}' updated successfully!")
         else:
            print("Word not found in the dictionary.")

    elif choice == "5":
        word = input("Enter the word to delete: ").strip().lower()
        if word in santosh_dictionary:
            del santosh_dictionary[word]
            print(f"Word '{word}' deleted successfully!")
        else:
            print("Word not found in the dictionary.")

    elif choice == "6":
        print("Exiting the program. see you later!")
        break

    else:
         print("Invalid choice. Please enter a number between 1 and 6.")





















            


