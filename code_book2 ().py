code_book ()
def add_contact():
    name = input("enter contact name")
    number=input("enter phone number:")
    code_book[name] = number
    print("contact added successfuly")
def view_contacts(): 
    if not code_book:
                               print("no contacts found./n")
    else:
                        print("obtain contacts")
    for name,number in code_book.items:
                              print(f"{name}: {number}")
    print ()