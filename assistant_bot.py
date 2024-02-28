import handlers 
from base import save_data, load_data

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = handlers.parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handlers.add_contact(args, book))
        elif command == "change":
            print(handlers.update_contact(args, book))
        elif command == "remove":
            print(handlers.delete_contact(args, book))    
        elif command == "phone":
            for result in handlers.find_contact(args, book):
              print(result)
        elif command == "all":
            for result in handlers.get_all_contacts(book):
              print(result)
        elif command == "delete":
            print(handlers.delete_record(args, book)) 
        elif command == "add-birthday":
            print(handlers.add_birthday(args, book))
        elif command == "show-birthday":
            print(handlers.show_birthday(args, book))
        elif command == "birthdays":
            for result in handlers.birthdays(book):
              print(result)
                              
        else:
            print("Invalid command.")
    save_data(book)        

if __name__ == "__main__":
    main()
    
