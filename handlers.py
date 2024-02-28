from classes import Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"Error: {e}" 

    return inner

@input_error
def parse_input(userInput):
    cmd, *args = userInput.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone = args
    name_in_book = book.find(name)
    if  not name_in_book:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f'Contact {name} added'
    else:
        name_in_book.add_phone(phone)
        return f"Phone added to contact {name}."
    
@input_error  
def update_contact(args, book):
    name, old_phone, new_phone = args
    name_in_book = book.find(name)
    
    if name_in_book:
        name_in_book.edit_phone(old_phone, new_phone)
        return "Contact updated"
    else:
        return f"Contact with name {name} not found"
    
@input_error
def delete_contact(args, book):
    name, phone = args
    name_in_book = book.find(name)
    if name_in_book:
        name_in_book.remove_phone(phone) 
        return f" {phone} is deleted"
    else:
         return f" {phone} not found"
 
@input_error    
def find_contact(args, book):
    name = args[0]
    name_in_book = book.find(name)
    if name_in_book:
     for phone in name_in_book.phones:
        yield f"Phone: {phone}"
    else:
        return f"Contact with name {name} not found" 
    
@input_error   
def get_all_contacts(book):
    for _, record in book.data.items():
       yield record

@input_error
def delete_record(args, book):
    name = args[0]
    name_in_book = book.find(name)
    if name_in_book:
        book.delete(name)
        return f" Record {name} deleted"
    else:
        return f"Contact with name {name} not found" 
    
@input_error
def add_birthday(args, book):
    name, date = args
    name_in_book = book.find(name)
    if name_in_book:
        name_in_book.add_birthday(date)
        return "Birthday added"  
    else:
        return f"Contact with name {name} not found" 
    
@input_error
def show_birthday(args, book):
    name = args[0]
    name_in_book = book.find(name)
    if name_in_book:
        return f"Birthday {name_in_book.birthday}"
    else:
        return f"Contact with name {name} not found"  
    
@input_error
def birthdays(book):
    for name, _ in book.data.items():
        name_in_book = book.find(name)
        date = name_in_book.birthdays(name)
        if not date:
            return "There are no birthdays next week"
        yield date                  