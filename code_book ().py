code_book ()
def add_contact():
    name = input("enter contact name")
    number=input("enter phone number:")
    code_book[name] = number
    print("contact added successfuly")