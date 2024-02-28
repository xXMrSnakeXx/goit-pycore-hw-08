from collections import UserDict
from datetime import datetime as dtdt
from helpers import get_upcoming_birthdays


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
           super().__init__(value)
        else: 
            raise ValueError ("Give me name")   
        
class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
         super().__init__(value)
        else:
            raise ValueError ("Not valid phone format") 
        
class Birthday(Field):
    def __init__(self, value):
        try:
            birthday_date = dtdt.strptime(value, "%d.%m.%Y").date()
            super().__init__(birthday_date)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")        

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
    
    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self, phone):
        for current_phone in self.phones:
            if current_phone.value == phone:
                self.phones.remove(current_phone)
                
    def edit_phone(self, old_phone, new_phone):
        Phone(new_phone)
        for current_phone in self.phones:
            if current_phone.value == old_phone:
                current_phone.value = new_phone
                break  
        else:
            raise ValueError('Phone not found')             
    
    def find_phone(self, phone):
        for current_phone in self.phones:
            if current_phone.value == phone:
                return current_phone
            
    def add_birthday(self, birthday_date):
        self.birthday = Birthday(birthday_date)
        return self.birthday        
                            
    def birthdays(self, name):
        if self.name.value == name and self.birthday:
            user = {"name" : self.name.value, "birthday": self.birthday.value.strftime("%d.%m.%Y")}
            birthdays = get_upcoming_birthdays(user)
            return birthdays                       

class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record
        
    def find(self, name):
       return self.data.get(name)
   
    def delete(self, name):
        if name in self.data:
            del self.data[name]  