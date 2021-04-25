import random

database = {}


def init():
    print("Welcome to bankPHP")

    have_account = int(input("Do you have an account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:

        login()
    elif have_account == 2:

        register()
    else:
        print("you have selected an invalid option")
        init()


def login():
    print("******** Login ********")

    account_number_from_user = int(input("what is your account number? \n"))
    password = input("what is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == account_number_from_user:
            if userDetails[3] == password:
                bank_operation(userDetails)

    login()
    print('Invalid account or password')


def register():

    print("**** Register ****")

    email = input("what is your email address? \n")
    first_name = input("what is your first name? \n")
    last_name = input("what is your last name? \n")
    password = input("create a password for yourself \n")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your Account has been created")
    print(" == === ======= ==== ===")
    print("Make sure you keep it %d" % account_number)
    print("Make sure you keep it safe")
    print(" == === ======= ==== ===")

    login()


def bank_operation(user):
    print("welcome %s %s" % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit  (2) withdrawal (3) Logout \n"))

    if selected_option == 1:

        deposit_operation()
    elif selected_option == 2:

        withdrawal_operation()
    elif selected_option == 3:

        logout()
    elif selected_option == 4:

        exit()
    else:

        print("InvalidOption selected")
    bank_operation(user)


def withdrawal_operation():
    print("withdrawal")


def deposit_operation():
    print("Deposit Operations")


def generate_account_number():

    return random.randrange(1111111111, 9999999999)


def logout():
    login()
