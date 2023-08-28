def bot_assistant():
    try:
        answer = input('==> ').lower().strip()
        command, *args = answer.split(' ')
        if answer in exit_answer:
            return exit_answer[3].capitalize()
        elif answer.startswith(OPERATIONS[0]):
            new_contact = add_contact(args)
            if new_contact:
                return new_contact
        elif answer.startswith(OPERATIONS[1]):
            update_contact = change_contact(args)
            return update_contact
        elif answer.startswith(OPERATIONS[2]):
            contact = show_contact(args)
            return contact
        elif answer.startswith(OPERATIONS[3]):
            return ""
        elif answer.startswith(OPERATIONS[4]):
            book = show_phone_book(answer)
            return book
        else:
            return "Sorry, don't know this command. Try again."
    except KeyboardInterrupt:
        return exit_answer[3].capitalize()


def main():
    while True:
        response = bot_assistant()
        print_answer(response)


def print_answer(message):
    print(message)


def input_error(func):
    def inner(s):
        try:
            return func(s)
        except KeyError:
            return 'Write correct value:'
        except ValueError:
            return 'Write correct value:'
        except IndexError:
            return 'Write correct value:'

    return inner


@input_error
def add_contact(args):
    phone_book.update({args[0]: args[1]})
    return f'Contact > {args[0].capitalize()} has been added'


@input_error
def change_contact(args):
    if phone_book.get(args[0]):
        answer = input('new phone number =>> ')
        phone_book.update({args[0]: answer})
        return f'Contact > {args[0].capitalize()} has been updated'
    else:
        return f"Sorry, {args[0].capitalize()} can't be found"


@input_error
def show_phone_book(_):
    phoneBook = ''
    for k, v in phone_book.items():
        phoneBook += '| {name}: {value}'.format(name=k, value=v)
    return phoneBook


@input_error
def show_contact(args):
    return f'{phone_book.get(args[0])}'


OPERATIONS = [
    'add',
    'change',
    'phone',
    'hello',
    'show all'
]
exit_answer = ['.', 'close', 'exit', 'good bye']
phone_book = {}

if __name__ == '__main__':
    main()

