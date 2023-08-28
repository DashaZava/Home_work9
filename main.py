def bot_assistant(answer):
    command, *args = answer.split(' ')
    handler = command_handlers.get(command)
    if handler:
        return handler(args)
    else:
        return "Sorry, don't know this command. Try again."

def add_contact(args):
    if len(args) != 2:
        return "Write correct value: name phone"
    phone_book[args[0]] = args[1]
    return f'Contact > {args[0].capitalize()} has been added'

def change_contact(args):
    if len(args) != 2:
        return "Write correct value: name phone"
    if args[0] in phone_book:
        new_phone = input('New phone number =>> ')
        phone_book[args[0]] = new_phone
        return f'Contact > {args[0].capitalize()} has been updated'
    else:
        return f"Sorry, {args[0].capitalize()} can't be found"

def show_phone_book(_):
    phoneBook = ''
    for name, phone in phone_book.items():
        phoneBook += f'| {name}: {phone}\n'
    return phoneBook

def show_contact(args):
    return phone_book.get(args[0], "Contact not found")

def print_answer(txt='How can I help you?'):
    print(txt)

OPERATIONS = [
    'add',
    'change',
    'phone',
    'hello',
    'show all'
]
exit_answer = ['.', 'close', 'exit', 'good bye']
phone_book = {}

command_handlers = {
    OPERATIONS[0]: add_contact,
    OPERATIONS[1]: change_contact,
    OPERATIONS[2]: show_contact,
    OPERATIONS[3]: lambda _: "",  # Empty function
    OPERATIONS[4]: show_phone_book
}

def main():
    while True:
        try:
            answer = input('==> ').lower().strip()
            response = bot_assistant(answer)
            print_answer(response)
        except KeyboardInterrupt:
            print_answer(f"{exit_answer[3].capitalize()}!")
            break

if __name__ == '__main__':
    main()
